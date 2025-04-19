import panphon

manual_class_override = {
    't': 'plosive', 'k': 'plosive', 's': 'fricative', 'd': 'plosive', 'b': 'plosive',
    'p': 'plosive', 'v': 'fricative', 'ʃ': 'fricative', 'ɡ': 'plosive', 'z': 'fricative',
    'x': 'fricative', 'f': 'fricative', 'ʒ': 'fricative', 'ɕ': 'fricative', 'ʂ': 'fricative',
    'ɖ': 'plosive', 'ʈ': 'plosive', 'ɣ': 'fricative', 'ʝ': 'fricative', 'ʁ': 'fricative'
}

ft = panphon.FeatureTable()

def get_sound_class(symbol):
    if symbol in manual_class_override:
        return manual_class_override[symbol]
    vectors = ft.word_to_vector_list(symbol, numeric=True)
    if not vectors:
        return 'unknown'
    features = vectors[0]
    names = ft.names
    def fval(name): return features[names.index(name)] if name in names else 0
    if fval('syl') == 1: return 'vowel'
    if fval('nas') == 1: return 'nasal'
    if fval('cont') == 1 and fval('syl') == 0: return 'fricative'
    if fval('delrel') == 0 and fval('syl') == 0: return 'plosive'
    if fval('approx') == 1 or (fval('son') == 1 and fval('syl') != 1 and fval('nas') != 1): return 'approximant'
    if fval('lat') == 1: return 'lateral'
    if fval('tap') == 1 or fval('flap') == 1: return 'tap_or_flap'
    if fval('trl') == 1: return 'trill'
    return 'other'

def sentiment_bin(score):
    if score <= -0.5: return 'very_negative'
    elif score <= -0.1: return 'moderately_negative'
    elif score < 0.1: return 'neutral'
    else: return 'positive'
