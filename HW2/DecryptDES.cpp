#include"iostream"
#include "string"
#include "vector"

using namespace std;
string CharKey = "";
string CharPlainText = "";
vector<int> Key;
vector<int> PlainText;
char Table[16] = { '0','1','2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C','D','E','F' };
string StringTable[16] = { "0","1","2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C","D","E","F" };
int IP[64] = { 58,50,42,34,26,18,10, 2,
				60,52,44,36,28,20,12, 4,
				62,54,46,38,30,22,14, 6,
				64,56,48,40,32,24,16, 8,
				57,49,41,33,25,17, 9, 1,
				59,51,43,35,27,19,11, 3,
				61,53,45,37,29,21,13, 5,
				63,55,47,39,31,23,15, 7 };
int IP_1[64] = { 40, 8,48,16,56,24,64,32,
					39, 7,47,15,55,23,63,31,
					38, 6,46,14,54,22,62,30,
					37, 5,45,13,53,21,61,29,
					36, 4,44,12,52,20,60,28,
					35, 3,43,11,51,19,59,27,
					34, 2,42,10,50,18,58,26,
					33, 1,41, 9,49,17,57,25 };
int E[48] = { 32, 1, 2, 3, 4, 5,
				 4, 5, 6, 7, 8, 9,
				 8, 9,10,11,12,13,
				12,13,14,15,16,17,
				16,17,18,19,20,21,
				20,21,22,23,24,25,
				24,25,26,27,28,29,
				28,29,30,31,32, 1 };
int PC_1[56] = { 57,49,41,33,25,17, 9,
					 1,58,50,42,34,26,18,
					10, 2,59,51,43,35,27,
					19,11, 3,60,52,44,36,
					63,55,47,39,31,23,15,
					 7,62,54,46,38,30,22,
					14, 6,61,53,45,37,29,
					21,13, 5,28,20,12, 4 };
int PC_2[48] = { 14,17,11,24, 1, 5,
					 3,28,15, 6,21,10,
					23,19,12, 4,26, 8,
					16, 7,27,20,13, 2,
					41,52,31,37,47,55,
					30,40,51,45,33,48,
					44,49,39,56,34,53,
					46,42,50,36,29,32 };
int P[32] = { 16, 7,20,21,29,12,28,17,
				 1,15,23,26, 5,18,31,10,
				 2, 8,24,14,32,27, 3, 9,
				19,13,30, 6,22,11, 4,25 };
int S1[4][16] = { 14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
					0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
					4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
					15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13 };
int S2[4][16] = { 15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
					3,13,4,7,14,2,8,14,12,0,1,10,6,9,11,5,
					0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
					13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9 };
int S3[4][16] = { 10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
					13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
					13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
					1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12 };
int S4[4][16] = { 7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
					13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
					10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
					3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14 };
int S5[4][16] = { 2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
					14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
					4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
					11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3 };
int S6[4][16] = { 12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
					10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
					9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
					4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13 };
int S7[4][16] = { 4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
					13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
					1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
					6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12 };
int S8[4][16] = { 13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
					1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
					7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
					2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11 };


vector<vector<int>> revrse(vector<vector<int>> Key)
{
	vector<vector<int>>temp;
	for (int i = 0; i < Key.size(); i++)
	{
		temp.push_back(Key[(Key.size() - i) - 1]);
	}
	return temp;
}

vector<int> KeyShift(vector<int> Ki, int Step)
{
	vector<int> C;
	vector<int> D;
	for (int i = 0; i < 28; i++)
	{
		C.push_back(Ki[i]);
		D.push_back(Ki[i + 28]);
	}
	if (Step == 0 || Step == 1 || Step == 8 || Step == 15)// shift one
	{
		//Cshift
		C.push_back(C[0]);
		for (int i = 0; i < 28; i++)
		{
			C[i] = C[i + 1];
		}
		C.pop_back();
		//Dshift
		D.push_back(D[0]);
		for (int i = 0; i < 28; i++)
		{
			D[i] = D[i + 1];
		}
		D.pop_back();
	}
	else  // shift TWO
	{
		//Cshift
		C.push_back(C[0]);
		for (int i = 0; i < 28; i++)
		{
			C[i] = C[i + 1];
		}
		C.pop_back();
		//Dshift
		D.push_back(D[0]);
		for (int i = 0; i < 28; i++)
		{
			D[i] = D[i + 1];
		}
		D.pop_back();
		//Cshift
		C.push_back(C[0]);
		for (int i = 0; i < 28; i++)
		{
			C[i] = C[i + 1];
		}
		C.pop_back();
		//Dshift
		D.push_back(D[0]);
		for (int i = 0; i < 28; i++)
		{
			D[i] = D[i + 1];
		}
		D.pop_back();
	}
	for (int i = 0; i < 28; i++)
	{
		Ki[i] = C[i];
		Ki[i + 28] = D[i];
	}
	return Ki;
}

vector<int> KeyPC_2(vector<int> Key)
{
	vector<int> KiOut;//48
	for (int i = 0; i < 48; i++)
	{
		KiOut.push_back(Key[PC_2[i] - 1]);
	}
	return KiOut;

}

vector<int> F_function(vector<int> Text, vector<int> Key)
{	//48
	int FourthRow[8] = { 0 };
	int ThirdColumn[8] = { 0 };
	int Out[8] = { 0 };
	vector<int> ExternText;
	for (int i = 0; i < 48; i++)
	{
		ExternText.push_back(Text[E[i] - 1]);
	}
	for (int i = 0; i < 48; i++)
	{
		ExternText[i] = ExternText[i] ^ Key[i];
	}
	/*cout << "ExternText ";
	for (int i = 0; i < 48; i++)
	{
		cout << ExternText[i];
	}
	cout << endl;*/


	///S_BBBBBOOOOOOXXXX
	vector<int> OutText;//32
	for (int i = 0; i < 32; i++)
	{
		OutText.push_back(0);
	}
	for (int i = 0; i < 8; i++)
	{
		int Out = 0;
		FourthRow[i] = ExternText[i * 6] * 2 + ExternText[i * 6 + 5];
		ThirdColumn[i] = (ExternText[i * 6 + 1] * 8) + (ExternText[i * 6 + 2] * 4) + (ExternText[i * 6 + 3] * 2) + (ExternText[i * 6 + 4]);
		/*cout << "Row " << FourthRow[i];
		cout << "Col " << ThirdColumn[i];*/
	}

	Out[0] = S1[FourthRow[0]][ThirdColumn[0]];
	Out[1] = S2[FourthRow[1]][ThirdColumn[1]];
	Out[2] = S3[FourthRow[2]][ThirdColumn[2]];
	Out[3] = S4[FourthRow[3]][ThirdColumn[3]];
	Out[4] = S5[FourthRow[4]][ThirdColumn[4]];
	Out[5] = S6[FourthRow[5]][ThirdColumn[5]];
	Out[6] = S7[FourthRow[6]][ThirdColumn[6]];
	Out[7] = S8[FourthRow[7]][ThirdColumn[7]];


	for (int i = 0; i < 8; i++)
	{
		OutText[i * 4] = (Out[i] / 8) % 2;
		OutText[i * 4 + 1] = (Out[i] / 4) % 2;
		OutText[i * 4 + 2] = (Out[i] / 2) % 2;
		OutText[i * 4 + 3] = Out[i] % 2;
	}
	/*cout << "OutText ";
	for (int i = 0; i < 32; i++)
	{
		cout << OutText[i];
	}
	cout << endl;*/
	vector<int> temp;
	for (int i = 0; i < 32; i++)
	{
		temp.push_back(OutText[P[i] - 1]);
	}

	for (int i = 0; i < 32; i++)
	{
		OutText[i] = temp[i];
	}
	/*cout << "OutOutText ";
	for (int i = 0; i < 32; i++)
	{
		cout << OutText[i];
	}
	cout << endl;*/
	return OutText;
}


int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "ERROR";
	}

	for (int i = 0; i < 16; i++)
	{
		CharKey += toupper(argv[1][i + 2]);
		CharPlainText += toupper(argv[2][i + 2]);
	}
	for (int i = 0; i < 16; i++) //char[] to bin
	{
		int TempChar = 0;
		int TempChar2 = 0;
		for (int j = 0; j < 16; j++)
		{
			if (Table[j] == CharKey[i])
			{
				TempChar = j;
			}
			if (Table[j] == CharPlainText[i])
			{
				TempChar2 = j;
			}
		}
		Key.push_back((TempChar / 8) % 2);
		Key.push_back((TempChar / 4) % 2);
		Key.push_back((TempChar / 2) % 2);
		Key.push_back((TempChar) % 2);

		PlainText.push_back((TempChar2 / 8) % 2);
		PlainText.push_back((TempChar2 / 4) % 2);
		PlainText.push_back((TempChar2 / 2) % 2);
		PlainText.push_back((TempChar2) % 2);
	}

	//Init Text
	vector<int> InitIPText;//64
	for (int i = 0; i < 64; i++)
	{
		InitIPText.push_back(PlainText[IP[i] - 1]);
	}

	vector<int> InLText;//32
	vector<int> InRText;//32
	for (int i = 0; i < 32; i++)
	{
		InLText.push_back(InitIPText[i]);
		InRText.push_back(InitIPText[i + 32]);
	}
	//Init Key
	vector<int> KeyComby;//56
	for (int i = 0; i < 56; i++)
	{
		KeyComby.push_back(Key[PC_1[i] - 1]);
	}

	vector<int> Ki;//48
	vector<int> OutLText;
	vector<int> OutRText;
	vector<int> Rtemp;
	for (int i = 0; i < 32; i++)
	{
		OutLText.push_back(2);
		OutRText.push_back(2);
	}
	vector<vector<int>> KeyTable;
	for (int i = 0; i < 16; i++)
	{
		KeyTable.push_back(KeyShift(KeyComby, i));
		KeyComby = KeyShift(KeyComby, i);
	}


	KeyTable = revrse(KeyTable);

	for (int i = 0; i < 16; i++)
	{
		//Key shift
		//KeyComby = KeyShift(KeyComby, i);

		//Key extern
		Ki = KeyPC_2(KeyTable[i]);//48

		//F function
		Rtemp = F_function(InRText, Ki);

		//Xor and exchange
		for (int j = 0; j < 32; j++)
		{
			OutRText[j] = InLText[j] ^ Rtemp[j];
		}
		OutLText = InRText;


		//to Next Step
		InLText = OutLText;
		InRText = OutRText;
	}



	vector<int> OutputComby;
	for (int i = 0; i < 32; i++)
	{
		OutputComby.push_back(OutRText[i]);
	}
	for (int i = 0; i < 32; i++)
	{
		OutputComby.push_back(OutLText[i]);
	}

	//finish Text
	vector<int> Outputtemp;
	for (int i = 0; i < 64; i++)
	{
		Outputtemp.push_back(OutputComby[IP_1[i] - 1]);
	}

	//To Hex
	string OutPut = "";
	for (int i = 0; i < 16; i++)
	{
		int temp = 0;
		temp += (Outputtemp[i * 4 + 0] * 8);
		temp += (Outputtemp[i * 4 + 1] * 4);
		temp += (Outputtemp[i * 4 + 2] * 2);
		temp += (Outputtemp[i * 4 + 3] * 1);
		OutPut += StringTable[temp];
	}

	for (int i = 0; i < OutPut.length(); i++)
	{
		OutPut[i] = tolower(OutPut[i]);
	}

	OutPut = "0x" + OutPut;
	cout << OutPut;
	return 0;
}