function ageCalculator() {
    let ondate = document.getElementById('ondate').value;
    let dob = document.getElementById('dob').value;
    ondatevalue = new Date(ondate)
    dobvalue = new Date(dob)
    if (ondate == null || ondate == '' && dob == null || dob == '') {
        document.getElementById("message").innerHTML = "**Choose a date please!";
        return false;
    } else {
        let diff_y = ondatevalue.getFullYear() - dobvalue.getFullYear()
        let diff_m = ondatevalue.getMonth() - dobvalue.getMonth()
        if (diff_m < 0) {
            diff_y = diff_y - 1;
            diff_m = 12 + diff_m;
            document.getElementById("message").innerHTML = "You are " + diff_y + " Year" + " and " + diff_m + " Month Old";
        } else {
            document.getElementById("message").innerHTML = "You are " + diff_y + " Year" + " and " + diff_m + " Month Old";
        }
    }
}
