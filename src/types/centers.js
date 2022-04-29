import { arrayOf, number, oneOfType, string } from 'prop-types';

export const CenterDetailsTitleType = {
  countyCode: string,
  lat: oneOfType([string, number]),
  lng: oneOfType([string, number]),
  locality: string,
  address: string,
  building: string,
  email: oneOfType([string, arrayOf(string)]),
  phoneNumber: string,
};

export default { CenterDetailsTitleType };
