import reflex as rx
from pcweb.components.icons.icons import get_icon


def install_command(command: str) -> rx.Component:
    return rx.el.button(
        get_icon(icon="copy", class_name="p-[5px]"),
        rx.text(
            "$" + command,
            as_="p",
            class_name="flex-grow flex-shrink min-w-0 font-small text-start truncate",
        ),
        title=command,
        on_click=rx.set_clipboard(command),
        class_name="flex items-center gap-1.5 border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small pr-1.5 border rounded-md w-full max-w-full text-slate-9 transition-bg cursor-pointer overflow-hidden",
    )


def repo(repo_url: str) -> rx.Component:
    return rx.link(
        get_icon(icon="new_tab", class_name="p-[5px]"),
        href=repo_url,
        is_external=True,
        class_name="border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small border border-solid rounded-md text-slate-9 hover:!text-slate-9 no-underline transition-bg cursor-pointer",
    )


def code_card(app: dict) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.el.a(
                rx.image(
                    src=app["image_url"],
                    loading="lazy",
                    alt="Image preview for app: " + app["name"],
                    class_name="w-full h-full duration-150 object-top object-cover hover:scale-105 transition-transform ease-out",
                ),
                href=app["demo_url"],
                is_external=True,
            ),
            class_name="relative border-slate-5 border-b border-solid w-full h-full overflow-hidden",
        ),
        rx.box(
            rx.box(
                rx.el.h4(
                    app["name"],
                    class_name="font-smbold text-slate-12 truncate",
                ),
                class_name="flex flex-row justify-between items-center gap-3 p-[0.625rem_0.75rem_0rem_0.75rem] w-full",
            ),
            rx.box(
                install_command("reflex init --template " + app["demo_url"]),
                rx.cond(app["source"], repo(app["source"])),
                rx.link(
                    get_icon(icon="eye", class_name="p-[5px]"),
                    href=app["demo_url"],
                    is_external=True,
                    class_name="border-slate-5 bg-slate-1 hover:bg-slate-3 shadow-small border border-solid rounded-md text-slate-9 hover:!text-slate-9 no-underline transition-bg cursor-pointer",
                ),
                class_name="flex flex-row items-center gap-[6px] p-[0rem_0.375rem_0.375rem_0.375rem] w-full",
            ),
            class_name="flex flex-col gap-[10px] w-full",
        ),
        style={
            "animation": "fade-in 0.35s ease-out",
            "@keyframes fade-in": {
                "0%": {"opacity": "0"},
                "100%": {"opacity": "1"},
            },
        },
        class_name="box-border flex flex-col border-slate-5 bg-slate-1 shadow-large border rounded-xl w-full h-[280px] overflow-hidden",
    )


def gallery_app_card(app: dict) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.link(
                rx.image(
                    src=app["image"],
                    loading="lazy",
                    alt="Image preview for app: " + app["title"],
                    class_name="w-full h-full duration-150 object-top object-cover hover:scale-105 transition-transform ease-out aspect-[1500/938]",
                ),
                href=f"/templates/{app['title'].replace(' ', '-').lower()}",
            ),
            class_name="relative border-slate-5 border-b border-solid w-full overflow-hidden h-[60%]",
        ),
        rx.box(
            rx.box(
                rx.el.h6(
                    app["title"],
                    class_name="font-smbold text-slate-12 truncate",
                ),
                rx.cond("template" in app,
                        rx.hstack(
                            rx.el.p(
                                "Template name: ",
                                rx.code(app.get('template', "")),
                                class_name="font-small text-slate-10 italic",
                            ),
                            rx.box(
                                get_icon(icon="copy", class_name="p-[5px]"),
                                on_click=rx.set_clipboard(app.get('template')),
                                style=rx.Style(
                                    {
                                        "background": rx.color("gray", 3),
                                        "border": "1px solid",
                                        "border-color": rx.color("gray", 5),
                                        "border-radius": "6px",
                                        "opacity": "1",
                                        "cursor": "pointer",
                                        "_hover": {
                                            "background": rx.color("gray", 4),
                                        },
                                        "transition": "background 0.250s ease-out",
                                        "&>svg": {
                                            "transition": "transform 0.250s ease-out, opacity 0.250s ease-out",
                                        },
                                        "_active": {
                                            "background": rx.color("gray", 5),
                                        },
                                    }
                                ),
                            )
                        ),

                        ),
                rx.text(
                    app["description"],
                    class_name="text-slate-10 font-small truncate text-pretty",
                ),
                rx.box(
                    rx.cond(
                        "Reflex" in app["author"],
                        rx.box(
                            rx.text(
                                "by",
                                class_name="text-slate-9 font-small",
                            ),
                            get_icon(icon="badge_logo"),
                            rx.text(
                                app["author"],
                                class_name="text-slate-9 font-small",
                            ),
                            class_name="flex flex-row items-center gap-1",
                        ),
                        rx.text(
                            f"by {app['author']}",
                            class_name="text-slate-9 font-small",
                        ),
                    ),
                    repo(app["demo"]),
                    class_name="flex flex-row items-center gap-[6px] justify-between w-full",
                ),
                class_name="flex flex-col justify-between items-start gap-1 p-[0.625rem_0.75rem_0.625rem_0.75rem] w-full h-full",
            ),
            class_name="flex flex-col gap-[10px] w-full h-full flex-1",
        ),
        style={
            "animation": "fade-in 0.35s ease-out",
            "@keyframes fade-in": {
                "0%": {"opacity": "0"},
                "100%": {"opacity": "1"},
            },
        },
        class_name="box-border flex flex-col border-slate-5 bg-slate-1 shadow-large border rounded-xl w-full h-[320px] overflow-hidden",
    )
