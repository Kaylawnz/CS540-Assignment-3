class PageFrameTable:
    def __init__(self, num_pages, num_frames):
        # Initialize the page/frame table with given sizes
        self.num_pages = num_pages
        self.num_frames = num_frames
        self.page_table = {}

    def map_page_to_frame(self, page_number, frame_number):
        # Map a page number to a frame number
        self.page_table[page_number] = frame_number

    def translate_address(self, logical_address):
        # Translate a logical address to a physical address
        page_number = (logical_address & 0xF000) >> 12
        offset = logical_address & 0xFFF

        if page_number in self.page_table:
            frame_number = self.page_table[page_number]
            physical_address = (frame_number << 12) | offset
            return f"Logical Address: {hex(logical_address)} => Page Number: {hex(page_number)}, Offset: {hex(offset)} => Physical Address: {hex(physical_address)}"
        else:
            return f"Page fault occurred for Logical Address: {hex(logical_address)}"


def main():
    # Initialize a page/frame table with 32 pages and 32 frames
    page_frame_table = PageFrameTable(32, 32)

    # Populate the table (for demonstration purposes)
    for i in range(32):
        page_frame_table.map_page_to_frame(i, i)

    # Sample logical addresses
    logical_addresses = [0x3A7F, 0xABCD, 0x5678]

    # Translate logical addresses to physical addresses and print the result
    for address in logical_addresses:
        print(page_frame_table.translate_address(address))


if __name__ == "__main__":
    main()
