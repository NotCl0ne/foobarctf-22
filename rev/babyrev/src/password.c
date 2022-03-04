
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int main(int argc, char *argv[])
{

	char * x = NULL;
	int result = TRUE;
	int password_length = 0;

	if(argc != 2)
	{
		printf("Usage: ./binary <key>\n");
		return -1;
	}

	

	x = argv[1];

	password_length = strlen(x);
	if (password_length != 42)
	{
		printf(";( INCORRECT\n");
		return -1;
	}

	if (!(x[13]+x[7]+x[8]==269))
	{
		result = FALSE;
	}
	if (!(x[0]-x[1]+x[14]+x[0]==165))
	{
		result = FALSE;
	}
	if (!(x[21]*x[16]+x[34]+x[38]==9482))
	{
		result = FALSE;
	}
	if (!(x[41]+x[8]*x[6]+x[23]==5500))
	{
		result = FALSE;
	}
	if (!(x[30]-x[30]-x[41]-x[21]==-223))
	{
		result = FALSE;
	}
	if (!(x[18]*x[4]*x[11]+x[19]==639710))
	{
		result = FALSE;
	}
	if (!(x[23]+x[33]*x[34]==6403))
	{
		result = FALSE;
	}
	if (!(x[18]*x[14]-x[33]==5072))
	{
		result = FALSE;
	}
	if (!(x[24]-x[39]-x[30]-x[22]==-110))
	{
		result = FALSE;
	}
	if (!(x[30]+x[10]-x[19]+x[1]==110))
	{
		result = FALSE;
	}
	if (!(x[15]-x[20]-x[41]==-169))
	{
		result = FALSE;
	}
	if (!(x[15]*x[35]-x[41]*x[8]==-10231))
	{
		result = FALSE;
	}
	if (!(x[11]*x[31]+x[36]-x[32]==8428))
	{
		result = FALSE;
	}
	if (!(x[25]+x[29]+x[40]==289))
	{
		result = FALSE;
	}
	if (!(x[7]-x[12]+x[24]==100))
	{
		result = FALSE;
	}
	if (!(x[21]*x[30]-x[6]==9262))
	{
		result = FALSE;
	}
	if (!(x[33]*x[38]*x[3]==480244))
	{
		result = FALSE;
	}
	if (!(x[20]-x[31]*x[0]-x[2]==-5954))
	{
		result = FALSE;
	}
	if (!(x[27]+x[12]*x[21]==5095))
	{
		result = FALSE;
	}
	if (!(x[6]+x[11]*x[8]-x[8]==10938))
	{
		result = FALSE;
	}
	if (!(x[34]-x[5]+x[7]*x[24]==5014))
	{
		result = FALSE;
	}
	if (!(x[40]-x[18]-x[2]==-83))
	{
		result = FALSE;
	}
	if (!(x[11]-x[31]+x[9]*x[24]==10114))
	{
		result = FALSE;
	}
	if (!(x[7]-x[7]-x[41]==-125))
	{
		result = FALSE;
	}
	if (!(x[28]+x[30]-x[16]*x[3]==-6543))
	{
		result = FALSE;
	}
	if (!(x[18]*x[25]-x[11]==5828))
	{
		result = FALSE;
	}
	if (!(x[9]*x[8]*x[11]==1089000))
	{
		result = FALSE;
	}
	if (!(x[3]*x[25]-x[29]*x[6]==2286))
	{
		result = FALSE;
	}
	if (!(x[36]-x[7]*x[33]==-3642))
	{
		result = FALSE;
	}
	if (!(x[32]-x[1]+x[20]==73))
	{
		result = FALSE;
	}
	if (!(x[39]+x[5]*x[4]==8307))
	{
		result = FALSE;
	}
	if (!(x[39]*x[0]*x[8]==515460))
	{
		result = FALSE;
	}
	if (!(x[12]-x[13]+x[31]==25))
	{
		result = FALSE;
	}
	if (!(x[41]+x[10]+x[18]+x[41]==351))
	{
		result = FALSE;
	}
	if (!(x[1]*x[14]+x[7]+x[22]==7624))
	{
		result = FALSE;
	}
	if (!(x[18]*x[24]+x[27]+x[14]==5500))
	{
		result = FALSE;
	}
	if (!(x[20]-x[41]*x[6]+x[18]==-5853))
	{
		result = FALSE;
	}
	if (!(x[33]-x[2]-x[31]*x[25]==-9585))
	{
		result = FALSE;
	}
	if (!(x[11]*x[18]*x[37]==353600))
	{
		result = FALSE;
	}
	if (!(x[7]+x[8]+x[17]-x[39]==192))
	{
		result = FALSE;
	}
	if (!(x[11]-x[35]-x[31]*x[9]==-8285))
	{
		result = FALSE;
	}
	if (!(x[23]-x[29]+x[39]==40))
	{
		result = FALSE;
	}
	if (!(x[28]+x[25]*x[10]*x[20]==530777))
	{
		result = FALSE;
	}
	if (!(x[29]*x[32]*x[3]==463914))
	{
		result = FALSE;
	}
	if (!(x[32]-x[22]+x[30]==98))
	{
		result = FALSE;
	}
	if (!(x[0]-x[13]+x[40]-x[38]==-74))
	{
		result = FALSE;
	}
	if (!(x[21]+x[17]-x[38]==108))
	{
		result = FALSE;
	}
	if (!(x[0]-x[41]*x[23]==-11804))
	{
		result = FALSE;
	}
	if (!(x[29]*x[2]*x[27]==997645))
	{
		result = FALSE;
	}
	if (!(x[25]-x[19]*x[35]==-7476))
	{
		result = FALSE;
	}
	if (!(x[16]-x[19]*x[7]==-5295))
	{
		result = FALSE;
	}
	if (!(x[33]+x[12]*x[26]+x[22]==2728))
	{
		result = FALSE;
	}
	if (!(x[24]+x[41]+x[32]==281))
	{
		result = FALSE;
	}
	if (!(x[31]*x[23]*x[14]==790020))
	{
		result = FALSE;
	}
	if (!(x[35]-x[6]*x[35]-x[14]==-3342))
	{
		result = FALSE;
	}
	if (!(x[31]+x[40]-x[25]*x[17]==-11148))
	{
		result = FALSE;
	}
	if (!(x[18]*x[36]+x[13]*x[19]==16364))
	{
		result = FALSE;
	}
	if (!(x[40]-x[5]+x[2]*x[18]==4407))
	{
		result = FALSE;
	}
	if (!(x[21]-x[25]+x[3]==55))
	{
		result = FALSE;
	}
	if (!(x[13]+x[14]+x[14]-x[2]==223))
	{
		result = FALSE;
	}
	if (!(x[36]*x[35]-x[5]*x[29]==-2449))
	{
		result = FALSE;
	}
	if (!(x[41]-x[39]+x[1]==135))
	{
		result = FALSE;
	}
	if (!(x[35]-x[0]*x[35]+x[0]==-4759))
	{
		result = FALSE;
	}
	if (!(x[8]-x[21]*x[10]-x[31]==-4776))
	{
		result = FALSE;
	}
	if (!(x[29]-x[24]+x[28]==126))
	{
		result = FALSE;
	}
	if (!(x[0]*x[10]-x[32]-x[8]==3315))
	{
		result = FALSE;
	}
	if (!(x[32]*x[28]+x[41]==5903))
	{
		result = FALSE;
	}
	if (!(x[37]-x[24]+x[32]==20))
	{
		result = FALSE;
	}
	if (!(x[20]*x[10]-x[15]+x[31]==4688))
	{
		result = FALSE;
	}
	if (!(x[36]-x[9]-x[18]*x[18]==-2721))
	{
		result = FALSE;
	}
	if (!(x[7]*x[9]+x[16]*x[30]==13876))
	{
		result = FALSE;
	}
	if (!(x[24]+x[34]+x[18]-x[7]==188))
	{
		result = FALSE;
	}
	if (!(x[27]*x[16]+x[20]==9310))
	{
		result = FALSE;
	}
	if (!(x[22]-x[30]-x[37]-x[9]==-211))
	{
		result = FALSE;
	}
	if (!(x[41]*x[4]*x[27]-x[38]==1491286))
	{
		result = FALSE;
	}
	if (!(x[35]-x[29]*x[8]+x[13]==-13131))
	{
		result = FALSE;
	}
	if (!(x[23]-x[7]-x[24]-x[22]==-107))
	{
		result = FALSE;
	}
	if (!(x[4]*x[37]*x[5]==560388))
	{
		result = FALSE;
	}
	if (!(x[17]*x[32]-x[15]==5295))
	{
		result = FALSE;
	}
	if (!(x[32]+x[23]*x[18]-x[5]==4927))
	{
		result = FALSE;
	}
	if (!(x[3]+x[8]*x[39]+x[39]==7397))
	{
		result = FALSE;
	}
	if (!(x[7]*x[25]-x[3]+x[36]==5597))
	{
		result = FALSE;
	}
	if (!(x[9]-x[24]-x[33]==-79))
	{
		result = FALSE;
	}
	if (!(x[30]+x[14]*x[36]==8213))
	{
		result = FALSE;
	}
	if (result == TRUE)
	{
		printf(":) CORRECT!\n");
		return 0;
	}

	if (result == FALSE)
	{
		printf(";( INCORRECT\n");
		return 0;
	}

	return 0;
}
