#include<iostream>
#include<cstdlib>
#include<string>
#include<vector>
using namespace std;
string CaeserDecrpt(string Key, string CinText)
{
	int CaesarShift = 0;
	CaesarShift = stoi(Key);
	for (int i = 0; i < CinText.length(); i++)
	{
		char temp = (CinText[i] - CaesarShift);
		if (temp < 'A')
		{
			temp = -('A' - temp) + 'A';
		}
		CinText[i] = (CinText[i] - CaesarShift);
	}
	for (int i = 0; i < CinText.length(); i++)
	{
		CinText[i] = toupper(CinText[i]);
	}
	return CinText;
}
string PlayfairDecrpt(string Key, string CinText)
{
	char playerFairMetrix[5][5];
	int alphabetlist[26] = { 0 };
	string ReSort = "";
	string Ciphertext = "";
	for (int i = 0; i < CinText.length(); i++)
	{
		CinText[i] = toupper(CinText[i]);
	}
	for (int i = 0; i < Key.length(); i++)
	{
		Key[i] = toupper(Key[i]);
	}
	for (int i = 0; i < Key.length(); i++)
	{
		if (alphabetlist[(int)(Key[i] - 'A')] == 0)
		{
			alphabetlist[(int)(Key[i] - 'A')] += 1;
			ReSort += Key[i];
		}
	}
	for (int i = 0; i < 26; i++)
	{
		if (alphabetlist[i] == 0)
		{
			ReSort += (char)(i + 'A');
		}
	}
	int TempCount = 0;
	int KeyLenght = Key.length();
	for (int i = 0; i < 26; i++)
	{
		if (ReSort[i] == 'J')
		{

		}
		else
		{
			playerFairMetrix[TempCount / 5][TempCount % 5] = ReSort[i];
			TempCount++;
		}
	}

	for (int count = 0; count < CinText.length(); count = count + 2)
	{
		int Ax, Ay, Bx, By;
		for (int i = 0; i < 5; i++)
		{
			for (int j = 0; j < 5; j++)
			{
				if (CinText[count] == playerFairMetrix[i][j])
				{
					Ax = i;
					Ay = j;
				}
				if (CinText[count + 1] == playerFairMetrix[i][j])
				{
					Bx = i;
					By = j;
				}
			}
		}
		if (Ax == Bx)
		{
			Ciphertext += playerFairMetrix[Ax][(Ay+4) % 5];
			Ciphertext += playerFairMetrix[Bx][(By +4) % 5];
		}
		else if (Ay == By)
		{
			Ciphertext += playerFairMetrix[(Ax +4) % 5][Ay];
			Ciphertext += playerFairMetrix[(Bx +4) % 5][By];
		}
		else
		{
			Ciphertext += playerFairMetrix[Ax][By];
			Ciphertext += playerFairMetrix[Bx][Ay];
		}
	}
	for (int i = 0; i < Ciphertext.length(); i++)
	{
		Ciphertext[i] = tolower(Ciphertext[i]);
	}
	return Ciphertext;
}
string VernamDecrpt(string Key, string CinText)
{
	string Ciphertext = "";
	for (int i = 0; i < CinText.length(); i++)
	{
		CinText[i] = toupper(CinText[i]);
	}
	for (int i = 0; i < Key.length(); i++)
	{
		Key[i] = toupper(Key[i]);
	}
	bool out = false;
	for (int i = 0; i < (CinText.length()/Key.length())+1; i++)
	{
		for (int j = 0; j < Key.length(); j++)
		{
			if (CinText.length() <= (i*Key.length() + j))
			{
				out = true;
				break;
			}
			char temp = (char)((int)((CinText[i*Key.length() + j] - 'A') ^ (int)(Key[j] - 'A')) + 'A');
			Ciphertext = Ciphertext + temp;
			Key[j] = temp;
		}
		if (out == true)
		{
			break;
		}
	}
	for (int i = 0; i < Ciphertext.length(); i++)
	{
		Ciphertext[i] = tolower(Ciphertext[i]);
	}
	return Ciphertext;
}
string RowDecrpt(string Key, string CinText)
{
	int* keyrow;
	string CipherText;
	char** MatrixOfText;
	MatrixOfText = new char*[Key.length()];
	int RowCount = 0;
	keyrow = new int[Key.length()];

	for (int i = 0; i < Key.length(); i++)
	{
		keyrow[(int)(Key[i] - '1')] = i;
		MatrixOfText[i] = new char[CinText.length() / Key.length() + 1];
	}
	for (int j = 0; j < Key.length(); j++)
	{
		for (int i = 0; i < (CinText.length() / Key.length()); i++)
		{
			MatrixOfText[keyrow[j]][i] = CinText[j*(CinText.length() / Key.length()) + i];
		}
	}
	for (int i = 0; i < (CinText.length() / Key.length()); i++)
	{
		for (int j = 0; j < Key.length(); j++)
		{
			CipherText += MatrixOfText[j][i];
		}
	}
	for (int i = 0; i < CipherText.length(); i++)
	{
		CipherText[i] = tolower(CipherText[i]);
	}
	return CipherText;
}
string Rail_fence(string Key, string CinText)
{
	string PlainText = "";
	int RailSize = 0;
	RailSize = stoi(Key);
	char** rail;
	rail = new char*[Key.size()];
	for (int i = 0; i < RailSize; i++)
	{
		rail[i] = new char[CinText.length()];
	}
	for (int i = 0; i < RailSize; i++)
	{
		for (int j = 0; j < CinText.length(); j++)
		{
			rail[i][j] = '\n';
		}
	}
	bool dir_down;
	int row = 0, col = 0;
	for (int i = 0; i < CinText.length(); i++)
	{

		if (row == 0)
		{
			dir_down = true;
		}
		if (row == RailSize - 1)
		{
			dir_down = false;
		}
		rail[row][col++] = '*';

		dir_down ? row++ : row--;
	}
	int index = 0;
	for (int i = 0; i < RailSize; i++)
	{
		for (int j = 0; j < CinText.length(); j++)
		{
			if (rail[i][j] == '*' && index < CinText.length())
			{
				rail[i][j] = CinText[index++];
			}
		}
	}
	string result;
	row = 0, col = 0;
	for (int i = 0; i < CinText.length(); i++)
	{
		if (row == 0)
		{
			dir_down = true;
		}
		if (row == RailSize - 1)
		{
			dir_down = false;
		}
		if (rail[row][col] != '*')
		{
			result.push_back(tolower(rail[row][col++]));
		}
		dir_down ? row++ : row--;
	}
	return result;
}
int main(int argc, char* argv[])
{
	string type(argv[1]);
	string Key(argv[2]);
	string CinText(argv[3]);
	for (int i = 4; i < argc; i++)
	{
		string temp(argv[i]);
		CinText = CinText + " " + temp;
	}
	string Ciphertext = "Nope";
	if (type == "caesar")
	{
		Ciphertext = CaeserDecrpt(Key, CinText);
	}
	else if (type == "playfair")
	{
		Ciphertext = PlayfairDecrpt(Key, CinText);
	}
	else if (type == "vernam")
	{
		Ciphertext = VernamDecrpt(Key, CinText);;
	}
	else if (type == "row")
	{
		Ciphertext = RowDecrpt(Key, CinText);
	}
	else if (type == "rail_fence")
	{
		Ciphertext = Rail_fence(Key, CinText);
	}
	cout << Ciphertext;
	system("PAUSE");
	return 0;
}