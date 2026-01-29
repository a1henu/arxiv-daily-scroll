---
layout: default
title: bi-modal textual prompt learning for vision-language models in remote sensing
---

# bi-modal textual prompt learning for vision-language models in remote sensing
**arXiv**：[2601.20675v1](https://arxiv.org/abs/2601.20675) · [PDF](https://arxiv.org/pdf/2601.20675.pdf)  
**作者**：Pankhi Kashyap, Mainak Singha, Biplab Banerjee  

**一句话要点**：提出BiMoRS双模态提示学习框架，以解决遥感图像中视觉语言模型泛化不足的问题。

**关键词**：遥感图像理解, 提示学习, 视觉语言模型, 双模态融合, 领域泛化

## 3 点简述
- 核心问题：现有提示学习方法在遥感图像中难以识别主导语义线索，泛化到新类别时效果不佳。
- 方法要点：利用冻结图像描述模型提取文本摘要，与视觉特征融合，通过轻量交叉注意力生成上下文提示。
- 实验或效果：在四个遥感数据集上评估，平均性能提升达2%，优于基线方法。

## 摘要（原文）

> Prompt learning (PL) has emerged as an effective strategy to adapt vision-language models (VLMs), such as CLIP, for downstream tasks under limited supervision. While PL has demonstrated strong generalization on natural image datasets, its transferability to remote sensing (RS) imagery remains underexplored. RS data present unique challenges, including multi-label scenes, high intra-class variability, and diverse spatial resolutions, that hinder the direct applicability of existing PL methods. In particular, current prompt-based approaches often struggle to identify dominant semantic cues and fail to generalize to novel classes in RS scenarios. To address these challenges, we propose BiMoRS, a lightweight bi-modal prompt learning framework tailored for RS tasks. BiMoRS employs a frozen image captioning model (e.g., BLIP-2) to extract textual semantic summaries from RS images. These captions are tokenized using a BERT tokenizer and fused with high-level visual features from the CLIP encoder. A lightweight cross-attention module then conditions a learnable query prompt on the fused textual-visual representation, yielding contextualized prompts without altering the CLIP backbone. We evaluate BiMoRS on four RS datasets across three domain generalization (DG) tasks and observe consistent performance gains, outperforming strong baselines by up to 2% on average. Codes are available at https://github.com/ipankhi/BiMoRS.

