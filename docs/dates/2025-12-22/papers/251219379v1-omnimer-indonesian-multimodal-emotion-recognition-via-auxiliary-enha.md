---
layout: default
title: OmniMER: Indonesian Multimodal Emotion Recognition via Auxiliary-Enhanced LLM Adaptation
---

# OmniMER: Indonesian Multimodal Emotion Recognition via Auxiliary-Enhanced LLM Adaptation
**arXiv**：[2512.19379v1](https://arxiv.org/abs/2512.19379) · [PDF](https://arxiv.org/pdf/2512.19379.pdf)  
**作者**：Xueming Yan, Boyan Xu, Yaochu Jin, Lixian Xiao, Wenlong Ye, Runyang Cai, Zeqi Zheng, Jingfa Liu, Aimin Yang  

**一句话要点**：提出OmniMER框架，通过辅助任务增强LLM适应，解决印尼语多模态情感识别中的跨模态不一致和长尾分布问题。

**关键词**：多模态情感识别, 印尼语数据集, 辅助任务增强, 跨模态不一致, 长尾分布, LLM适应

## 3 点简述
- 核心问题：印尼语多模态情感识别研究不足，面临跨模态不一致和长尾类分布等现实挑战。
- 方法要点：基于Qwen2.5-Omni构建框架，引入文本、视频和音频的辅助感知任务以增强模态特定线索识别。
- 实验或效果：在IndoMER数据集上，情感分类和情感识别的Macro-F1分别提升7.6和22.1绝对点，并在跨语言评估中展示泛化性。

## 摘要（原文）

> Indonesian, spoken by over 200 million people, remains underserved in multimodal emotion recognition research despite its dominant presence on Southeast Asian social media platforms. We introduce IndoMER, the first multimodal emotion recognition benchmark for Indonesian, comprising 1,944 video segments from 203 speakers with temporally aligned text, audio, and visual annotations across seven emotion categories. The dataset exhibits realistic challenges including cross-modal inconsistency and long-tailed class distributions shaped by Indonesian cultural communication norms. To address these challenges, we propose OmniMER, a multimodal adaptation framework built upon Qwen2.5-Omni that enhances emotion recognition through three auxiliary modality-specific perception tasks: emotion keyword extraction for text, facial expression analysis for video, and prosody analysis for audio. These auxiliary tasks help the model identify emotion-relevant cues in each modality before fusion, reducing reliance on spurious correlations in low-resource settings. Experiments on IndoMER show that OmniMER achieves 0.582 Macro-F1 on sentiment classification and 0.454 on emotion recognition, outperforming the base model by 7.6 and 22.1 absolute points respectively. Cross-lingual evaluation on the Chinese CH-SIMS dataset further demonstrates the generalizability of the proposed framework. The dataset and code are publicly available. https://github.com/yanxm01/INDOMER

