---
layout: default
title: Robust Multicentre Detection and Classification of Colorectal Liver Metastases on CT: Application of Foundation Models
---

# Robust Multicentre Detection and Classification of Colorectal Liver Metastases on CT: Application of Foundation Models
**arXiv**：[2601.07585v1](https://arxiv.org/abs/2601.07585) · [PDF](https://arxiv.org/pdf/2601.07585.pdf)  
**作者**：Shruti Atul Mali, Zohaib Salahuddin, Yumeng Zhang, Andre Aichert, Xian Zhong, Henry C. Woodruff, Maciej Bobowicz, Katrine Riklund, Juozas Kupčinskas, Lorenzo Faggioni, Roberto Francischello, Razvan L Miclea, Philippe Lambin  

**一句话要点**：提出基于基础模型的AI流程，用于多中心CT中结直肠肝转移的稳健检测与分类。

**关键词**：结直肠肝转移检测, 基础模型应用, 多中心CT分析, 不确定性量化, 病灶检测分类

## 3 点简述
- 核心问题：结直肠肝转移在多中心CT检测中可靠性差，影响癌症死亡率。
- 方法要点：集成UMedPT基础模型，通过MLP和FCOS头进行患者分类和病灶检测，并量化不确定性。
- 实验或效果：在测试集上分类AUC达0.90，检测模型整体识别69.1%病灶，排除不确定案例可提升性能。

## 摘要（原文）

> Colorectal liver metastases (CRLM) are a major cause of cancer-related mortality, and reliable detection on CT remains challenging in multi-centre settings. We developed a foundation model-based AI pipeline for patient-level classification and lesion-level detection of CRLM on contrast-enhanced CT, integrating uncertainty quantification and explainability. CT data from the EuCanImage consortium (n=2437) and an external TCIA cohort (n=197) were used. Among several pretrained models, UMedPT achieved the best performance and was fine-tuned with an MLP head for classification and an FCOS-based head for lesion detection. The classification model achieved an AUC of 0.90 and a sensitivity of 0.82 on the combined test set, with a sensitivity of 0.85 on the external cohort. Excluding the most uncertain 20 percent of cases improved AUC to 0.91 and balanced accuracy to 0.86. Decision curve analysis showed clinical benefit for threshold probabilities between 0.30 and 0.40. The detection model identified 69.1 percent of lesions overall, increasing from 30 percent to 98 percent across lesion size quartiles. Grad-CAM highlighted lesion-corresponding regions in high-confidence cases. These results demonstrate that foundation model-based pipelines can support robust and interpretable CRLM detection and classification across heterogeneous CT data.

