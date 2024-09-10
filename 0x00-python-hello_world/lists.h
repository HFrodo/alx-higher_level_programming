#ifndef LISTS_H
#define LISTS_H

ssize_t write(int fd, const void *buf, size_t count);
int printf(const char *format, ...);
int putchar(int char);
int puts(const char *str);
void *malloc(size_t size);
void free(void *ptr);

#endif
