from transformers.configuration_xlm_roberta import XLMRobertaConfig
from transformers.modeling_xlm_roberta import XLM_ROBERTA_PRETRAINED_MODEL_ARCHIVE_MAP

from melior_transformers.classification.transformer_models.roberta_model import (
    RobertaForSequenceClassification,
)


class XLMRobertaForSequenceClassification(RobertaForSequenceClassification):
    config_class = XLMRobertaConfig
    pretrained_model_archive_map = XLM_ROBERTA_PRETRAINED_MODEL_ARCHIVE_MAP