# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
This documentation was automatically generated using original comments in
Doxygen format. As some C types and data structures cannot be directly mapped
into Python types, some non-trivial type conversion could have place.
Basically a type is replaced with another one that has the closest match, and
sometimes one argument of generated function comprises several arguments of the
original function (usually two). Apparently Doxygen comments do not mention
this fact, so here is a list of all known conversions so far:

  FILE * -> file
  const int16 *SDATA, size_t NSAMP -> str

Also functions having error code as the return value and returning effective
value in one of its arguments are transformed so that the effective value is
returned in a regular fashion and run-time exception is being thrown in case of
negative error code.
"""


from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pocketsphinx', [dirname(__file__)])
        except ImportError:
            import _pocketsphinx
            return _pocketsphinx
        if fp is not None:
            try:
                _mod = imp.load_module('_pocketsphinx', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pocketsphinx = swig_import_helper()
    del swig_import_helper
else:
    import _pocketsphinx
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


import sphinxbase
class Hypothesis(_object):
    """Proxy of C Hypothesis struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Hypothesis, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Hypothesis, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hypstr"] = _pocketsphinx.Hypothesis_hypstr_set
    __swig_getmethods__["hypstr"] = _pocketsphinx.Hypothesis_hypstr_get
    if _newclass:
        hypstr = _swig_property(_pocketsphinx.Hypothesis_hypstr_get, _pocketsphinx.Hypothesis_hypstr_set)
    __swig_setmethods__["best_score"] = _pocketsphinx.Hypothesis_best_score_set
    __swig_getmethods__["best_score"] = _pocketsphinx.Hypothesis_best_score_get
    if _newclass:
        best_score = _swig_property(_pocketsphinx.Hypothesis_best_score_get, _pocketsphinx.Hypothesis_best_score_set)
    __swig_setmethods__["prob"] = _pocketsphinx.Hypothesis_prob_set
    __swig_getmethods__["prob"] = _pocketsphinx.Hypothesis_prob_get
    if _newclass:
        prob = _swig_property(_pocketsphinx.Hypothesis_prob_get, _pocketsphinx.Hypothesis_prob_set)

    def __init__(self, hypstr, best_score, prob):
        """__init__(Hypothesis self, char const * hypstr, int best_score, int prob) -> Hypothesis"""
        this = _pocketsphinx.new_Hypothesis(hypstr, best_score, prob)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_Hypothesis
    __del__ = lambda self: None
Hypothesis_swigregister = _pocketsphinx.Hypothesis_swigregister
Hypothesis_swigregister(Hypothesis)

class Segment(_object):
    """Proxy of C Segment struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Segment, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Segment, name)
    __repr__ = _swig_repr
    __swig_setmethods__["word"] = _pocketsphinx.Segment_word_set
    __swig_getmethods__["word"] = _pocketsphinx.Segment_word_get
    if _newclass:
        word = _swig_property(_pocketsphinx.Segment_word_get, _pocketsphinx.Segment_word_set)
    __swig_setmethods__["ascore"] = _pocketsphinx.Segment_ascore_set
    __swig_getmethods__["ascore"] = _pocketsphinx.Segment_ascore_get
    if _newclass:
        ascore = _swig_property(_pocketsphinx.Segment_ascore_get, _pocketsphinx.Segment_ascore_set)
    __swig_setmethods__["lscore"] = _pocketsphinx.Segment_lscore_set
    __swig_getmethods__["lscore"] = _pocketsphinx.Segment_lscore_get
    if _newclass:
        lscore = _swig_property(_pocketsphinx.Segment_lscore_get, _pocketsphinx.Segment_lscore_set)
    __swig_setmethods__["lback"] = _pocketsphinx.Segment_lback_set
    __swig_getmethods__["lback"] = _pocketsphinx.Segment_lback_get
    if _newclass:
        lback = _swig_property(_pocketsphinx.Segment_lback_get, _pocketsphinx.Segment_lback_set)
    __swig_setmethods__["prob"] = _pocketsphinx.Segment_prob_set
    __swig_getmethods__["prob"] = _pocketsphinx.Segment_prob_get
    if _newclass:
        prob = _swig_property(_pocketsphinx.Segment_prob_get, _pocketsphinx.Segment_prob_set)
    __swig_setmethods__["start_frame"] = _pocketsphinx.Segment_start_frame_set
    __swig_getmethods__["start_frame"] = _pocketsphinx.Segment_start_frame_get
    if _newclass:
        start_frame = _swig_property(_pocketsphinx.Segment_start_frame_get, _pocketsphinx.Segment_start_frame_set)
    __swig_setmethods__["end_frame"] = _pocketsphinx.Segment_end_frame_set
    __swig_getmethods__["end_frame"] = _pocketsphinx.Segment_end_frame_get
    if _newclass:
        end_frame = _swig_property(_pocketsphinx.Segment_end_frame_get, _pocketsphinx.Segment_end_frame_set)

    def fromIter(itor):
        """fromIter(ps_seg_t * itor) -> Segment"""
        return _pocketsphinx.Segment_fromIter(itor)

    if _newclass:
        fromIter = staticmethod(fromIter)
    __swig_getmethods__["fromIter"] = lambda x: fromIter
    __swig_destroy__ = _pocketsphinx.delete_Segment
    __del__ = lambda self: None

    def __init__(self):
        """__init__(Segment self) -> Segment"""
        this = _pocketsphinx.new_Segment()
        try:
            self.this.append(this)
        except:
            self.this = this
Segment_swigregister = _pocketsphinx.Segment_swigregister
Segment_swigregister(Segment)

def Segment_fromIter(itor):
    """Segment_fromIter(ps_seg_t * itor) -> Segment"""
    return _pocketsphinx.Segment_fromIter(itor)

class NBest(_object):
    """Proxy of C NBest struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NBest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NBest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nbest"] = _pocketsphinx.NBest_nbest_set
    __swig_getmethods__["nbest"] = _pocketsphinx.NBest_nbest_get
    if _newclass:
        nbest = _swig_property(_pocketsphinx.NBest_nbest_get, _pocketsphinx.NBest_nbest_set)

    def fromIter(itor):
        """fromIter(ps_nbest_t * itor) -> NBest"""
        return _pocketsphinx.NBest_fromIter(itor)

    if _newclass:
        fromIter = staticmethod(fromIter)
    __swig_getmethods__["fromIter"] = lambda x: fromIter

    def hyp(self):
        """hyp(NBest self) -> Hypothesis"""
        return _pocketsphinx.NBest_hyp(self)

    __swig_destroy__ = _pocketsphinx.delete_NBest
    __del__ = lambda self: None

    def __init__(self):
        """__init__(NBest self) -> NBest"""
        this = _pocketsphinx.new_NBest()
        try:
            self.this.append(this)
        except:
            self.this = this
NBest_swigregister = _pocketsphinx.NBest_swigregister
NBest_swigregister(NBest)

def NBest_fromIter(itor):
    """NBest_fromIter(ps_nbest_t * itor) -> NBest"""
    return _pocketsphinx.NBest_fromIter(itor)

class SegmentIterator(_object):
    """Proxy of C SegmentIterator struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SegmentIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SegmentIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ptr"] = _pocketsphinx.SegmentIterator_ptr_set
    __swig_getmethods__["ptr"] = _pocketsphinx.SegmentIterator_ptr_get
    if _newclass:
        ptr = _swig_property(_pocketsphinx.SegmentIterator_ptr_get, _pocketsphinx.SegmentIterator_ptr_set)

    def __init__(self, ptr):
        """__init__(SegmentIterator self, ps_seg_t * ptr) -> SegmentIterator"""
        this = _pocketsphinx.new_SegmentIterator(ptr)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_SegmentIterator
    __del__ = lambda self: None

    def next(self):
        """next(SegmentIterator self) -> Segment"""
        return _pocketsphinx.SegmentIterator_next(self)

SegmentIterator_swigregister = _pocketsphinx.SegmentIterator_swigregister
SegmentIterator_swigregister(SegmentIterator)

class NBestIterator(_object):
    """Proxy of C NBestIterator struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NBestIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NBestIterator, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ptr"] = _pocketsphinx.NBestIterator_ptr_set
    __swig_getmethods__["ptr"] = _pocketsphinx.NBestIterator_ptr_get
    if _newclass:
        ptr = _swig_property(_pocketsphinx.NBestIterator_ptr_get, _pocketsphinx.NBestIterator_ptr_set)

    def __init__(self, ptr):
        """__init__(NBestIterator self, ps_nbest_t * ptr) -> NBestIterator"""
        this = _pocketsphinx.new_NBestIterator(ptr)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_NBestIterator
    __del__ = lambda self: None

    def next(self):
        """next(NBestIterator self) -> NBest"""
        return _pocketsphinx.NBestIterator_next(self)

NBestIterator_swigregister = _pocketsphinx.NBestIterator_swigregister
NBestIterator_swigregister(NBestIterator)

class Decoder(_object):
    """Proxy of C Decoder struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Decoder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Decoder, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(Decoder self) -> Decoder
        __init__(Decoder self, Config config) -> Decoder
        """
        this = _pocketsphinx.new_Decoder(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_Decoder
    __del__ = lambda self: None

    def reinit(self, config):
        """reinit(Decoder self, Config config)"""
        return _pocketsphinx.Decoder_reinit(self, config)


    def load_dict(self, fdict, ffilter, format):
        """load_dict(Decoder self, char const * fdict, char const * ffilter, char const * format)"""
        return _pocketsphinx.Decoder_load_dict(self, fdict, ffilter, format)


    def save_dict(self, dictfile, format):
        """save_dict(Decoder self, char const * dictfile, char const * format)"""
        return _pocketsphinx.Decoder_save_dict(self, dictfile, format)


    def add_word(self, word, phones, update):
        """add_word(Decoder self, char const * word, char const * phones, int update)"""
        return _pocketsphinx.Decoder_add_word(self, word, phones, update)


    def lookup_word(self, word):
        """lookup_word(Decoder self, char const * word) -> char *"""
        return _pocketsphinx.Decoder_lookup_word(self, word)


    def get_lattice(self):
        """get_lattice(Decoder self) -> Lattice"""
        return _pocketsphinx.Decoder_get_lattice(self)


    def get_config(self):
        """get_config(Decoder self) -> Config"""
        return _pocketsphinx.Decoder_get_config(self)


    def default_config():
        """default_config() -> Config"""
        return _pocketsphinx.Decoder_default_config()

    if _newclass:
        default_config = staticmethod(default_config)
    __swig_getmethods__["default_config"] = lambda x: default_config

    def file_config(path):
        """file_config(char const * path) -> Config"""
        return _pocketsphinx.Decoder_file_config(path)

    if _newclass:
        file_config = staticmethod(file_config)
    __swig_getmethods__["file_config"] = lambda x: file_config

    def start_stream(self):
        """start_stream(Decoder self)"""
        return _pocketsphinx.Decoder_start_stream(self)


    def start_utt(self):
        """start_utt(Decoder self)"""
        return _pocketsphinx.Decoder_start_utt(self)


    def end_utt(self):
        """end_utt(Decoder self)"""
        return _pocketsphinx.Decoder_end_utt(self)


    def process_raw(self, SDATA, no_search, full_utt):
        """process_raw(Decoder self, void const * SDATA, bool no_search, bool full_utt) -> int"""
        return _pocketsphinx.Decoder_process_raw(self, SDATA, no_search, full_utt)


    def decode_raw(self, fin):
        """decode_raw(Decoder self, FILE * fin) -> int"""
        return _pocketsphinx.Decoder_decode_raw(self, fin)


    def set_rawdata_size(self, size):
        """set_rawdata_size(Decoder self, size_t size)"""
        return _pocketsphinx.Decoder_set_rawdata_size(self, size)


    def get_rawdata(self):
        """get_rawdata(Decoder self)"""
        return _pocketsphinx.Decoder_get_rawdata(self)


    def hyp(self):
        """hyp(Decoder self) -> Hypothesis"""
        return _pocketsphinx.Decoder_hyp(self)


    def get_fe(self):
        """get_fe(Decoder self) -> FrontEnd"""
        return _pocketsphinx.Decoder_get_fe(self)


    def get_feat(self):
        """get_feat(Decoder self) -> Feature"""
        return _pocketsphinx.Decoder_get_feat(self)


    def get_in_speech(self):
        """get_in_speech(Decoder self) -> bool"""
        return _pocketsphinx.Decoder_get_in_speech(self)


    def get_fsg(self, name):
        """get_fsg(Decoder self, char const * name) -> FsgModel"""
        return _pocketsphinx.Decoder_get_fsg(self, name)


    def set_fsg(self, name, fsg):
        """set_fsg(Decoder self, char const * name, FsgModel fsg)"""
        return _pocketsphinx.Decoder_set_fsg(self, name, fsg)


    def set_jsgf_file(self, name, path):
        """set_jsgf_file(Decoder self, char const * name, char const * path)"""
        return _pocketsphinx.Decoder_set_jsgf_file(self, name, path)


    def get_kws(self, name):
        """get_kws(Decoder self, char const * name) -> char const *"""
        return _pocketsphinx.Decoder_get_kws(self, name)


    def set_kws(self, name, keyfile):
        """set_kws(Decoder self, char const * name, char const * keyfile)"""
        return _pocketsphinx.Decoder_set_kws(self, name, keyfile)


    def set_keyphrase(self, name, keyphrase):
        """set_keyphrase(Decoder self, char const * name, char const * keyphrase)"""
        return _pocketsphinx.Decoder_set_keyphrase(self, name, keyphrase)


    def set_allphone_file(self, name, lmfile):
        """set_allphone_file(Decoder self, char const * name, char const * lmfile)"""
        return _pocketsphinx.Decoder_set_allphone_file(self, name, lmfile)


    def get_lm(self, name):
        """get_lm(Decoder self, char const * name) -> NGramModel"""
        return _pocketsphinx.Decoder_get_lm(self, name)


    def set_lm(self, name, lm):
        """set_lm(Decoder self, char const * name, NGramModel lm)"""
        return _pocketsphinx.Decoder_set_lm(self, name, lm)


    def set_lm_file(self, name, path):
        """set_lm_file(Decoder self, char const * name, char const * path)"""
        return _pocketsphinx.Decoder_set_lm_file(self, name, path)


    def get_logmath(self):
        """get_logmath(Decoder self) -> LogMath"""
        return _pocketsphinx.Decoder_get_logmath(self)


    def set_search(self, search_name):
        """set_search(Decoder self, char const * search_name)"""
        return _pocketsphinx.Decoder_set_search(self, search_name)


    def get_search(self):
        """get_search(Decoder self) -> char const *"""
        return _pocketsphinx.Decoder_get_search(self)


    def n_frames(self):
        """n_frames(Decoder self) -> int"""
        return _pocketsphinx.Decoder_n_frames(self)


    def seg(self):
        """seg(Decoder self) -> SegmentList"""
        return _pocketsphinx.Decoder_seg(self)


    def nbest(self):
        """nbest(Decoder self) -> NBestList"""
        return _pocketsphinx.Decoder_nbest(self)

Decoder_swigregister = _pocketsphinx.Decoder_swigregister
Decoder_swigregister(Decoder)

def Decoder_default_config():
    """Decoder_default_config() -> Config"""
    return _pocketsphinx.Decoder_default_config()

def Decoder_file_config(path):
    """Decoder_file_config(char const * path) -> Config"""
    return _pocketsphinx.Decoder_file_config(path)

class Lattice(_object):
    """Proxy of C Lattice struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Lattice, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Lattice, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(Lattice self, char const * path) -> Lattice
        __init__(Lattice self, Decoder decoder, char * path) -> Lattice
        """
        this = _pocketsphinx.new_Lattice(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_Lattice
    __del__ = lambda self: None

    def write(self, path):
        """write(Lattice self, char const * path)"""
        return _pocketsphinx.Lattice_write(self, path)


    def write_htk(self, path):
        """write_htk(Lattice self, char const * path)"""
        return _pocketsphinx.Lattice_write_htk(self, path)

Lattice_swigregister = _pocketsphinx.Lattice_swigregister
Lattice_swigregister(Lattice)

class NBestList(_object):
    """Proxy of C NBestList struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NBestList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NBestList, name)
    __repr__ = _swig_repr

    def __init__(self, ptr):
        """__init__(NBestList self, ps_decoder_t * ptr) -> NBestList"""
        this = _pocketsphinx.new_NBestList(ptr)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __iter__(self):
        """__iter__(NBestList self) -> NBestIterator"""
        return _pocketsphinx.NBestList___iter__(self)

    __swig_destroy__ = _pocketsphinx.delete_NBestList
    __del__ = lambda self: None
NBestList_swigregister = _pocketsphinx.NBestList_swigregister
NBestList_swigregister(NBestList)

class SegmentList(_object):
    """Proxy of C SegmentList struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SegmentList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SegmentList, name)
    __repr__ = _swig_repr

    def __init__(self, ptr):
        """__init__(SegmentList self, ps_decoder_t * ptr) -> SegmentList"""
        this = _pocketsphinx.new_SegmentList(ptr)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __iter__(self):
        """__iter__(SegmentList self) -> SegmentIterator"""
        return _pocketsphinx.SegmentList___iter__(self)

    __swig_destroy__ = _pocketsphinx.delete_SegmentList
    __del__ = lambda self: None
SegmentList_swigregister = _pocketsphinx.SegmentList_swigregister
SegmentList_swigregister(SegmentList)

# This file is compatible with both classic and new-style classes.


