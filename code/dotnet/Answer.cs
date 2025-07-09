using System.Text.Json;

// Load data
var users = JsonSerializer.Deserialize<Dictionary<string, object>[]>(File.ReadAllText("../../data/users.json"));
var exercises = JsonSerializer.Deserialize<Dictionary<string, object>[]>(File.ReadAllText("../../data/exercises.json"));
var workouts = JsonSerializer.Deserialize<Dictionary<string, object>[]>(File.ReadAllText("../../data/workouts.json"));


/** Candidate TODO: Write code to answer questions **/


// In total, how many pounds have these athletes Bench Pressed?
var answerOne = "foo";

// How many pounds did Barry Moore Back Squat in 2016?
var answerTwo = "bar";

// In what month of 2017 did Barry Moore Back Squat the most total weight?
var answerThree = "baz";

// What is Abby Smith's Bench Press PR weight?
// (PR defined as the most the person has ever lifted for that exercise, regardless of reps performed.)
var answerFour = "qux";

var results = new Dictionary<string, string> {
    {"Q1", answerOne},
    {"Q2", answerTwo},
    {"Q3", answerThree},
    {"Q4", answerFour}
};

Console.WriteLine(JsonSerializer.Serialize(results));
