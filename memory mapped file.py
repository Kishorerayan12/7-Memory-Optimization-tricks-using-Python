import mmap as custommmap

length = 10000  # no of bytes the file should read


# Open the file in binary mode and create a memory-mapped file
with open("/home/kishorerayan12/The.Great.Dictator.English-WWW.MY-SUBS.CO.srt", 'rb') as file:
    # Map the entire file into memory
    with custommmap.mmap(file.fileno(), 0, access=custommmap.ACCESS_READ) as mmapped_file:
        # Seek to the 1000th position
        mmapped_file.seek(1000)

        # Read the first 1000 bytes from the 1000th position
        content = mmapped_file.read(2000)

        # Print or process the content as needed
        print(content.decode('utf-8'))