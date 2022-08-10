int fieldsExpected = /*nums of row*/
string fileOut     = /*fielOut path*/
string fileIn      = /*fielIn path*/

string[] lines = System.IO.File.ReadAllLines(fileIn);
List<string> newLines = new List<string>();

for (int i = 0; i < lines.Length; i++) {
    string temp = lines[i];
    string[] fields = temp.Split('|');

    while (fields.Length < fieldsExpected && i < (lines.Length - 1)) {
        i++;
        temp += lines[i];
        fields = temp.Split('|');
    }
    newLines.Add(temp);
}

System.IO.File.WriteAllLines(fileOut, newLines.ToArray());