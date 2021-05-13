import moment from "moment";

export default function dateSorter(dateOne, dateTwo) {
  const dateOneDate = moment(dateOne, 'Do MMMM YYYY').format();
  const dateTwoDate = moment(dateTwo, 'Do MMMM YYYY').format();
  if (dateOneDate < dateTwoDate) return 1;
  if (dateOneDate > dateTwoDate) return -1;
  return 0;
}
