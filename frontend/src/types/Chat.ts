import { Message } from "./Message"
import { User } from "./User"

export type Chat = {
    id: number,
    last_message: Message | null,
    unseen_count: number,
    user: User,
    viewed_at: string | null,
    created_at: string
}

export type APIGetChats = {
    chats: Chat[]
}

export type APICreateChat = {
    chats: Chat
}

export type APIDeleteChat = {
    success: boolean
}

export type UpdateChatEvent = {
    type?: 'delete',
    query: {
        chat_id?: number,
        users: number[]
    }
}
