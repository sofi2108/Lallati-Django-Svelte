const get = () => {
  return localStorage.getItem("id") || undefined;
};

const save = (id) => {
  localStorage.setItem("id", String(id));
};

const getCartItems = async (cart) => {
  const res = await fetch(`http://127.0.0.1:8000/carts/${cart}/items/`);
  return res.json();
};

const getCartDetails = async (cart) => {
  const res = await fetch(`http://127.0.0.1:8000/carts/${cart}/`);
  return res.json();
};

const LallatiApi = {
  get,
  save,
  getCartItems,
  getCartDetails,
};

export default LallatiApi;
