const month = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
];

// Функция для изменения формата числа (по разрядам)
function numberFormatter(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
}

// Функция для изменения формата dateTime
function dateFormatter(date) {
    const dateFormat = new Date(date);
    
    const getMonth = dateFormat.getMonth();
    const getDay = dateFormat.getDate();

    return `${getDay} ${month[getMonth]}`
}

function dateTimeFormatter(dateTime) {
    const dateFormat = new Date(dateTime);

    const getMonth = dateFormat.getMonth();
    const getDay = dateFormat.getDate();
    const getTime = `${dateFormat.getHours()}:${dateFormat.getMinutes()}`

    return `${getDay} ${month[getMonth]} - ${getTime}`
}

export {
    numberFormatter,
    dateFormatter,
    dateTimeFormatter
}