function findUser(users, name) {
    for (let i = 0; i < users.length; i++) {
        if (users[i].name = name) {
            return users[i];
        }
    }

    return null;
}

const users = [
    { name: "Ali", age: 22 },
    { name: "Leyla", age: 25 }
];

console.log(findUser(users, "Leyla"));