import { writable } from "svelte/store";

export const cart = writable();
export const items = writable([]);
export const cartDetails = writable({});
export const user_info = writable({});
