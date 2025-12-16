const getStudentsByLocation = (students, city) => {
    return students.filter(students => students.location === city);
};

export default getStudentsByLocation;