#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <gnu/libc-version.h>

#define	GPIO1	"35" //using evaluation board and jumper to SODIMM 133
//Delay for the simple delay function
#define DELAY_SIMPLE 160 //in usec

//Delay for the elaborated delay function
//200000.00 and 16000.00 for 400us square wave
#define DELAY_ELABORATED_WANTED 200000.00
#define OFFSET_ELABORATED 16000.00
#define DELAY_ELABORATED (DELAY_ELABORATED_WANTED-OFFSET_ELABORATED)
#define DELAY_FREE_PROCESSOR 40

#define DELAY_NANOSLEEP_NSEC 200000.00
#define NSEC_PER_SEC    1000000000

void simple_delay_blink(FILE *fp);
void enhanced_delay_blink(FILE *fp);
void nanosleep_delay_blink(FILE *fp);

int main(int argc, char **argv) {
	puts (gnu_get_libc_version ());
	FILE *fp; //pointer to file handling

	//starting app
	puts("Starting the gpio squarewave v0.1");

	//export GPIO pins so they can be used
	fp = fopen("/sys/class/gpio/export", "w");
	fputs(GPIO1, fp); fflush(fp);
	fclose(fp);

	//configure pins
	fp = fopen("/sys/class/gpio/gpio35/direction", "w");
	fputs("out", fp); fclose(fp);//configure as OUTPUT

	//blink infinite loop
	fp = fopen("/sys/class/gpio/gpio35/value", "w");
	//simple_delay_blink(fp);
	enhanced_delay_blink(fp);
	//nanosleep_delay_blink(fp);
	return EXIT_SUCCESS;
}

void simple_delay_blink(FILE *fp){
	while(1){
		fputs("1", fp); fflush(fp);//write GPIO HIGH and flush the buffer
		usleep(DELAY_SIMPLE);//wait 1 second

		fputs("0", fp); fflush(fp); //write GPIO LOW and flush the buffer
		usleep(DELAY_SIMPLE);//wait 1 second
	}
}

void enhanced_delay_blink(FILE *fp){
	struct timespec start, stop;
	while(1){
		fputs("1", fp); fflush(fp);//write GPIO HIGH and flush the buffer
		clock_gettime( CLOCK_REALTIME, &start);
		usleep(DELAY_FREE_PROCESSOR);//free processor for some time
		clock_gettime( CLOCK_REALTIME, &stop);
		while(( 1000000000.00 * (stop.tv_sec - start.tv_sec) + ( stop.tv_nsec - start.tv_nsec ) ) < DELAY_ELABORATED){//just wait here until it is time
			clock_gettime( CLOCK_REALTIME, &stop);
		}

		fputs("0", fp); fflush(fp); //write GPIO LOW and flush the buffer
		clock_gettime( CLOCK_REALTIME, &start);
		usleep(DELAY_FREE_PROCESSOR);//free processor for some time
		clock_gettime( CLOCK_REALTIME, &stop);
		while(( 1000000000.00 * (stop.tv_sec - start.tv_sec) + ( stop.tv_nsec - start.tv_nsec ) ) < DELAY_ELABORATED){//just wait here until it is time
			clock_gettime( CLOCK_REALTIME, &stop);
		}
	}
}

void nanosleep_delay_blink(FILE *fp){
	struct timespec tnow;
	clock_gettime(0, &tnow);
	tnow.tv_sec++;//set the first time for 1 second before start
	while(1){
		clock_nanosleep(CLOCK_REALTIME, TIMER_ABSTIME, &tnow, NULL);
		fputs("1", fp); fflush(fp);//write GPIO HIGH and flush the buffer
		tnow.tv_nsec += DELAY_NANOSLEEP_NSEC;//delay half period of the wave
		while (tnow.tv_nsec >= NSEC_PER_SEC) {
			tnow.tv_nsec -= NSEC_PER_SEC;
			tnow.tv_sec++;
		}

		clock_nanosleep(CLOCK_REALTIME, TIMER_ABSTIME, &tnow, NULL);
		fputs("0", fp); fflush(fp);//write GPIO LOW and flush the buffer
		tnow.tv_nsec += DELAY_NANOSLEEP_NSEC;//delay half period of the wave
		while (tnow.tv_nsec >= NSEC_PER_SEC) {
			tnow.tv_nsec -= NSEC_PER_SEC;
			tnow.tv_sec++;
		}
	}
}

