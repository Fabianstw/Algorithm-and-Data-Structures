#include <iostream>
#include <fstream>
#include <unordered_set>
#include "algo-helper-runtime/json.hpp"
#include <unordered_map>

using namespace std;

using json = nlohmann::json;
std::unordered_set<std::string> dictionarywords;

void loadDictionary(const std::string& dictionaryFile) {
    std::ifstream file(dictionaryFile);

    if (file.is_open()) {
        json jsonDictionary;
        file >> jsonDictionary;

        for (const auto& word : jsonDictionary) {
            dictionarywords.insert(word.get<std::string>());
        }

        file.close();
    }

}

std::unordered_map<char, int> stringToLetterCount(const std::string& inputString) {
    std::unordered_map<char, int> letterCountMap;

    for (char letter : inputString) {
        // Increment the count for each letter
        letterCountMap[letter]++;
    }

    return letterCountMap;
}

int main() {
    std::string filePath = "/Users/fabianstiewe/Desktop/Coding/Github Public/Algorithm-and-Data-Structures/leetcode/cpp/algo-helper-runtime/words_alpha.txt";

    // make an vector string empty
    vector<string> words_len8;
    vector<string> words_len9;
    vector<string> words_len10;
    vector<string> words_len11;
    vector<string> words_len12;

    std::ifstream inputFile(filePath);

    if (!inputFile.is_open()) {
        std::cerr << "Error opening file: " << filePath << std::endl;
        return 1;
    }

    std::string line;
    int count = 0;
    while (std::getline(inputFile, line)) {
        if (count > 100) {
            break;
        }
        count++;
        // Print each line to check if it's being read correctly
        std::cout << "Read line: ";
        for (char character : line) {
            std::cout << character << " (" << static_cast<int>(character) << ") ";  // Print each character and its ASCII value
        }
        std::cout << std::endl;

        if (line.size() == 8) {
            words_len8.push_back(line);
            // convert the string to a set
            std::unordered_map<char, int> letterCountMap = stringToLetterCount(line);
            if (letterCountMap.size() == 3) {
                // check if one letter repeats one time, one twice and the last 5 times
                // if so, add it to the vector
            }
        }
    }


    return 0;
}
