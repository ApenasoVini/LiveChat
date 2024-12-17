"use client";

import { useAuthStore } from "@/stores/authStore";
import { useChatStore } from "@/stores/chatStore";
import { User } from "@/types/User";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";

type Props = {
  user: User | null;
  children: React.ReactNode;
};

export const MainLayout = ({ user, children }: Props) => {
  const auth = useAuthStore();
  const { showChatsList, setShowChatsList } = useChatStore();
  const [loading, setLoading] = useState(true);
  const pathname = usePathname();

  useEffect(() => {
    if (user)
  });
};
