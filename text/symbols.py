from acoustic_feature_extractor.data.phoneme import OjtPhoneme

_pad = "_"

# Export all symbols:
symbols = [_pad] + list(OjtPhoneme.phoneme_list)
accent_symbols = [_pad] + ["0", "1"]
