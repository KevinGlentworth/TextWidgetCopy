from tkinter.font import Font

def textwidgetcopy(from_widget = None, to_widget = None, clear_out_widget: bool=True, copy_all: bool = False):
    text_detail = from_widget.get('1.0', 'end')
    out_state = to_widget.cget('state')
    to_widget.config(state='normal')
    if clear_out_widget:
        to_widget.delete('1.0', 'end')
    to_widget.insert('1.0', text_detail)
    if copy_all:
        to_widget.config(width=from_widget.cget('width'),
                               height=from_widget.cget('height'),
                               fg=from_widget.cget('fg'),
                               bg=from_widget.cget('bg'),
                               bd=from_widget.cget('bd'),
                               relief=from_widget.cget('relief'))
        i_font=Font(font=from_widget['font']).actual
        modifier:str = ''
        if i_font()['weight'] == 'bold':
            modifier += 'bold '
        if i_font()['slant'] == 'italic':
            modifier += 'italic '
        if i_font()['underline'] == 1:
            modifier += 'underline '
        if i_font()['overstrike'] == 1:
            modifier += 'overstrike '
        to_widget.config(font = (i_font()['family'], i_font()['size'], modifier))
    text_info = from_widget.dump('1.0', 'end', tag=True)
    tag_dict: dict = {}
    for ti in text_info:
        match ti[0]:
            case 'tagon':
                print(f'tagon   {ti[1]} {ti[2]}')
                tag_dict[ti[1]] = ti[2]
            case 'tagoff':
                print(f'tagoff  {ti[1]} {ti[2]}')
                to_widget.tag_add(ti[1], tag_dict[ti[1]], ti[2])
                del tag_dict[ti[1]]
            case 'mark':
                print(f'mark    {ti[1]} {ti[2]}')
            case 'image':
                print(f'image   {ti[1]} {ti[2]}')
            case 'window':
                print(f'window  {ti[1]} {ti[2]}')
            case _:
                print(f'invalid {ti[0]}')
    tag_names = to_widget.tag_names()
    for tag_name in reversed(tag_names):
        print('to', tag_name)
    tag_names = from_widget.tag_names()
    for tag_name in reversed(tag_names):
        if tag_name == 'sel':
            continue
        tag_details = from_widget.tag_config(tag_name)
        for key, detail in tag_details.items():
            print(f'tagname={tag_name}, key={key}, detail={detail[4]}')
            if detail[4] != '':
                p: dict = {detail[0]: detail[4]}
                # if detail[4] =='bold' or detail[4] == 'italic':
                #     print('bold or italic found')
                #     font = Font(font=to_widget['font']).actual
                    # print('out2:', font())
                # print(f'{tag_name}: detail: "{detail[0]}", "{detail[1]}", "{detail[2]}", "{detail[3]}", "{detail[4]}"')
                print(f'tagname={tag_name}, p={p}')
                if tag_name == 'sel':
                    to_widget.tag_add('sel', '2.3', '2.7')
                    to_widget.tag_config('sel', foreground='yellow', background='red')
                else:
                    to_widget.tag_config(tag_name, p)
    to_widget.config(state=out_state)


