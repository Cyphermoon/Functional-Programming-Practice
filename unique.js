// const colors = ["red", "red", "green", "blue", "blue"]

const reduceUniqueColors = colors.reduce((unique, color) => unique.indexOf(color) === -1 ? [...unique, color] : unique, []);

const filterUniqueColors = colors.filter(color)

// let arrays = [1, 2, 3, 1, 3, 5]

// function returnDuplicate(arrays) {

// 	let internalArray = arrays.filter((value, index) => {
// 		arrays.splice(index, 1)
// 		return value in arrays
// 	})

// 	return internalArray
// }


// console.log(returnDuplicate(arrays))
// console.log(arrays)


