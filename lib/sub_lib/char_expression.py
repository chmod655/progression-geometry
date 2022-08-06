
arr = {
    'letter_normal' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()',
    'letter_superscript' : 'ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾',
    'letter_subscript' : 'ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎'
}

class CharComponent:
    def __init__(self) -> None:
         pass
    def superscript(text):
            normal = arr['letter_normal']
            super_s = arr['letter_superscript']
            res = text.maketrans(''.join(normal), ''.join(super_s))
            return text.translate(res)

    def subscript(text):
        normal = arr['letter_normal']
        sub_s = arr['letter_subscript']
        res = text.maketrans(''.join(normal), ''.join(sub_s))
        return text.translate(res)