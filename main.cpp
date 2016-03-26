//  ArrayContainer
//
//  Created by Ben Masi on 10/1/15.

#include <iostream>

#include <iomanip>

#include <cmath>

#include <cstdlib>

using namespace std;

class Element {
public:
    Element (string Udata)
    {udata=Udata; }
    string* putElement (string*, string, int);
    string findElement (string*, string, int);
    string* getList (string*, int);
    string* deleteElement (string*, string, int);
    
private:
    string udata;
    
    
};

string* Element::putElement (string* oldArray, string data, int length){
    int i;
    string* newArray = NULL;
    newArray = new string[length + 1];
    
    for (i = 0; i < length; i++){
        *(newArray+i) = *(oldArray+i);
    }
    
    newArray[length] = data;
    
    delete [] oldArray;
    oldArray = newArray;
    
    cout << data << " Has been added to the array" << endl;
    
    return oldArray;
}

string Element::findElement (string* Array, string searchData, int length){
    int i;
    string foundTerm;
    for (i = 0; i < length; i++){
        if (Array[i] == searchData){
            foundTerm = Array[i];
            break;
        }
        else
            foundTerm = " ";
        }

        return foundTerm;
    
}


string* Element::deleteElement (string* oldArray, string data, int length){
    int i, j, k, index;
    string* newArray;
    newArray = new string[length - 1];
    
    
    for (i = 0; i < length; i++){
        if (oldArray[i] == data){
            index = i;
        break;
        }
        
        else
            cout << "Sorry, term could not be found in the array" << endl;
    }
    
    
    for (j = 0; j < index; j++){
        *(newArray+j) = *(oldArray+j);
    }
    
    for (k = (index + 1); k < length; k++){
        *(newArray+(k-1)) = *(oldArray+k);
    }
    
    
    delete [] oldArray;
    oldArray = newArray;
    
    return oldArray;
        
};



int main() {
    string* Array = NULL;
    int arrayLength;
    int i;
    cout << "How many elements would you like in your array?"<< endl;
    cin >> arrayLength;
    
    Array = new string[arrayLength];
    
    for (i = 0; i < arrayLength; i++){
        if (!cin.eof() && cin.good()){
            cout << "Please enter a string or EOF to terminate" << endl;
            cin >> *(Array + i);
        }
        else if (!cin.eof()) {
            cout << "Invalid Input" << endl;
        }
        
        else {
            cout << "Heap exhausted." << endl;
        }
    }
    
    string udata, searchTerm;
    bool cont = true;
    char sel;
    string* temp = NULL;
    while (!cin.eof()&&cin.good()&&cont == true) {
        cout << "Enter your function: Add, Exit, Find, List, Delete: ";
        cin >> sel;
        if (!cin.eof()) {
            switch (sel) {
                case 'A': case 'a': {
                    cout << "Enter a string to add to the array ";
                    cin >> udata;
                    if (!cin.eof() && cin.good()){
                        Element add(udata);
                        temp = add.putElement(Array, udata, arrayLength);
                        
                        if (temp != NULL){
                            Array = temp;
                            arrayLength++;
                        }
                        else
                            cout << "Sorry, no more room in the heap" << endl;
                    }
                    
                    else
                        if (!cin.good())
                            cout << "Invalid data" << endl;
                    break;
                }
                case 'E': case 'e': {
                    cont = false;
                    break;
                }
                case 'F': case 'f': {
                    cout << "Please enter the string you are looking for: ";
                    cin >> udata;
                    if (!cin.eof() && cin.good()){
                        Element find(udata);
                        searchTerm = find.findElement(Array, udata, arrayLength);
                        if (searchTerm != " ")
                            cout << "Your term was found in the array" << endl;
                        else
                            cout << "Sorry your term could not be found in the array" << endl;
                        break;
                    }
                case 'L': case 'l': {
                    cout << "Your array currently contains: " << endl;
                    int i;
                    
                    for (i = 0; i < arrayLength; i++){
                      cout << Array[i] << ", ";
                    }
                    cout << endl;
                    break;
                }
                case 'D': case 'd': {
                    cout << "Enter a string to delete from your array ";
                    cin >> udata;
                    if (!cin.eof() && cin.good()){
                        Element del(udata);
                        temp = del.deleteElement(Array, udata, arrayLength);
                    }
                    
                        
                        if (temp != NULL){
                            Array = temp;
                            cout << udata << " has been deleted from the array" << endl;
                            arrayLength--;
                        }
                        
                    else
                        if (!cin.good())
                            cout << "Invalid data" << endl;
                    break;
                    
                }
                default: {
                    cout << "Invalid selection entered." << endl;
                    break;
                }
                }
            }
        }
    }
        system ("PAUSE");
        return 0;
    }

