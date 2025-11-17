---
layout: default
title: Enhancing Meme Emotion Understanding with Multi-Level Modality Enhancement and Dual-Stage Modal Fusion
---

# Enhancing Meme Emotion Understanding with Multi-Level Modality Enhancement and Dual-Stage Modal Fusion
**arXiv**：[2511.11126v1](https://arxiv.org/abs/2511.11126) · [PDF](https://arxiv.org/pdf/2511.11126.pdf)  
**作者**：Yi Shi, Wenlong Meng, Zhenyuan Guo, Chengkun Wei, Wenzhi Chen  

**一句话要点**：提出MemoDetector框架，通过多级模态增强与双阶段融合提升表情包情感理解

**关键词**：表情包情感理解, 多模态融合, 大型语言模型, 隐含意义挖掘, 双阶段融合

## 3 点简述
- 核心问题：表情包情感理解中缺乏细粒度多模态融合策略和隐含意义挖掘
- 方法要点：使用MLLM增强文本，并设计双阶段模态融合策略
- 实验或效果：在MET-MEME和MOOD数据集上F1分数分别提升4.3%和3.4%

## 摘要（原文）

> With the rapid rise of social media and Internet culture, memes have become a popular medium for expressing emotional tendencies. This has sparked growing interest in Meme Emotion Understanding (MEU), which aims to classify the emotional intent behind memes by leveraging their multimodal contents. While existing efforts have achieved promising results, two major challenges remain: (1) a lack of fine-grained multimodal fusion strategies, and (2) insufficient mining of memes' implicit meanings and background knowledge. To address these challenges, we propose MemoDetector, a novel framework for advancing MEU. First, we introduce a four-step textual enhancement module that utilizes the rich knowledge and reasoning capabilities of Multimodal Large Language Models (MLLMs) to progressively infer and extract implicit and contextual insights from memes. These enhanced texts significantly enrich the original meme contents and provide valuable guidance for downstream classification. Next, we design a dual-stage modal fusion strategy: the first stage performs shallow fusion on raw meme image and text, while the second stage deeply integrates the enhanced visual and textual features. This hierarchical fusion enables the model to better capture nuanced cross-modal emotional cues. Experiments on two datasets, MET-MEME and MOOD, demonstrate that our method consistently outperforms state-of-the-art baselines. Specifically, MemoDetector improves F1 scores by 4.3\% on MET-MEME and 3.4\% on MOOD. Further ablation studies and in-depth analyses validate the effectiveness and robustness of our approach, highlighting its strong potential for advancing MEU. Our code is available at https://github.com/singing-cat/MemoDetector.

