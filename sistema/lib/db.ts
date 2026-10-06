import { PrismaClient } from "@prisma/client";

// no next dev o arquivo recarrega a cada alteracao. guardar o cliente no globalThis
// evita abrir uma conexao nova com o banco a cada recarga
const global = globalThis as unknown as { prisma?: PrismaClient };

export const prisma = global.prisma ?? new PrismaClient();

if (process.env.NODE_ENV !== "production") global.prisma = prisma;
