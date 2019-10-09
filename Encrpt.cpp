#include<iostream>
#include<cstdlib>
#include<string>
#include<vector>
using namespace std;
string CaesarEncrpt(string Key, string CinText)
{
	int CaesarShift = 0;
	CaesarShift = stoi(Key);
	for (int i = 0; i < CinText.length(); i++)
	{
		CinText[i] = (((CinText[i]-'A') + CaesarShift) % 26)+'A';
	}
	for (int i = 0; i < CinText.length(); i++)
	{
		CinText[i] = toupper(CinText[i]);
	}
	return CinText;
}
string PlayfairEncrpt(string Key, string CinText)
{
	char playerFairMetrix[5][5];
	int alphabetlist[26] = { 0 };
	string ReSort = "";
	string PianText = "";
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
			PianText += playerFairMetrix[Ax][(Ay + 1) % 5];
			PianText += playerFairMetrix[Bx][(By + 1) % 5];
		}
		else if (Ay == By)
		{
			PianText += playerFairMetrix[(Ax + 1) % 5][Ay];
			PianText += playerFairMetrix[(Bx + 1) % 5][By];
		}
		else
		{
			PianText += playerFairMetrix[Ax][By];
			PianText += playerFairMetrix[Bx][Ay];
		}
	}
	return PianText;
}
string VernamEncrpt(string Key, string CinText)
{
	string PlainText = "";
	for (int i = 0; i < CinText.length(); i++)
	{
		CinText[i] = toupper(CinText[i]);
	}
	for (int i = 0; i < Key.length(); i++)
	{
		Key[i] = toupper(Key[i]);
	}
	Key = Key + CinText;
	for (int i = 0; i < CinText.length(); i++)
	{
		PlainText = PlainText+(char)((int)((CinText[i]-'A') ^ (int)(Key[i]-'A'))+'A');
	}
	for (int i = 0; i < PlainText.length(); i++)
	{
		PlainText[i] = toupper(PlainText[i]);
	}
	return PlainText;
}
string RowEncrpt(string Key, string CinText)
{
	int* keyrow;
	string PrinText;
	char** MatrixOfText;
	MatrixOfText = new char*[Key.length()];
	int RowCount = 0;
	keyrow = new int[Key.length()];
	for (int i = 0; i < Key.length(); i++)
	{
		keyrow[(int)(Key[i] - '1')] = i;
		MatrixOfText[i] = new char[CinText.length() / Key.length() + 1];
	}
	for (int j = 0; j < (CinText.length() / Key.length()); j++)
	{
		for (int i = 0; i < Key.length(); i++)
		{
			if ((j*Key.length() + i) > CinText.length());
			{
				MatrixOfText[j][i] = ' ';
			}
			MatrixOfText[j][i] = CinText[j*Key.length() + i];
		}
	}
	for (int j = 0; j < Key.length(); j++)
	{
		for (int i = 0; i < (CinText.length() / Key.length()); i++)
		{
			PrinText += MatrixOfText[i][keyrow[j]];
		}
	}
	for (int i = 0; i < PrinText.length(); i++)
	{
		PrinText[i] = toupper(PrinText[i]);
	}
	return PrinText;
}
string Rail_fence(string Key, string CinText)
{
	string PlainText = "";
	int RailSize = 0;
	RailSize = stoi(Key);
	char** Rail;
	Rail = new char*[RailSize];
	for (int i = 0; i < RailSize; i++)
	{
		Rail[i] = new char[(CinText.length())];
	}
	for (int i = 0; i < RailSize; i++)
	{
		for (int j = 0; j < CinText.length(); j++)
		{
			Rail[i][j] = '\n';
		}
	}

	bool dir_down = false;
	int row = 0, col = 0;

	for (int i = 0; i < CinText.length(); i++)
	{
		if (row == 0 || row == RailSize - 1)
		{
			dir_down = !dir_down;
		}

		Rail[row][col++] = CinText[i];

		dir_down ? row++ : row--;
	}

	for (int i = 0; i < RailSize; i++)
	{
		for (int j = 0; j < CinText.length(); j++)
		{
			if (Rail[i][j] != '\n')
			{
				PlainText.push_back(Rail[i][j]);
			}
		}
	}
	return PlainText;
}
int main(int argc, char* argv[])
{
	if (argc != 4)
	{
		return 1;
	}
	string type(argv[1]);
	string Key(argv[2]);
	string CinText(argv[3]);
	string PlainText = "Nope";
	if (type == "caesar")
	{
		PlainText = CaesarEncrpt(Key, CinText);
		cout << PlainText;
	}
	else if (type == "playfair")
	{
		PlainText = PlayfairEncrpt(Key, CinText);
		cout << PlainText;
	}
	else if (type == "vernam")
	{
		PlainText = VernamEncrpt(Key, CinText);
		cout << PlainText;
	}
	else if (type == "row")
	{
		PlainText = RowEncrpt(Key, CinText);
		cout << PlainText;
	}
	else if (type == "rail_fence")
	{
		PlainText = Rail_fence(Key, CinText);
		cout << PlainText;
	}
	system("PAUSE");
	return 0;
}