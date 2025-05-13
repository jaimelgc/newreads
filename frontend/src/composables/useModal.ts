import { ref } from 'vue';

export function useModal<T = null>() {
  const isOpen = ref(false);
  const payload = ref<T | null>(null);

  const open = (data?: T) => {
    payload.value = data ?? null;
    isOpen.value = true;
  };

  const close = () => {
    isOpen.value = false;
    payload.value = null;
  };

  return {
    isOpen,
    payload,
    open,
    close,
  };
}