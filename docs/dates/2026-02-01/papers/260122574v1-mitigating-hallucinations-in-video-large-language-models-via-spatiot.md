---
layout: default
title: Mitigating Hallucinations in Video Large Language Models via Spatiotemporal-Semantic Contrastive Decoding
---

# Mitigating Hallucinations in Video Large Language Models via Spatiotemporal-Semantic Contrastive Decoding
**arXiv**：[2601.22574v1](https://arxiv.org/abs/2601.22574) · [PDF](https://arxiv.org/pdf/2601.22574.pdf)  
**作者**：Yuansheng Gao, Jinman Zhao, Tong Zhang, Xingguo Xu, Han Bao, Zonghui Wang, Wenzhi Chen  

**一句话要点**：提出时空语义对比解码策略以缓解视频大语言模型的幻觉问题

**关键词**：视频大语言模型, 幻觉缓解, 对比解码, 时空特征, 语义关联, 视频理解

## 3 点简述
- 核心问题：视频大语言模型在视频理解等任务中易产生与视频内容或事实不符的幻觉输出
- 方法要点：通过破坏视频特征的时空一致性和语义关联构建负特征，在推理时与原特征进行对比解码以抑制幻觉
- 实验或效果：实验表明该方法有效减少幻觉，同时保持模型的通用视频理解和推理能力

## 摘要（原文）

> Although Video Large Language Models perform remarkably well across tasks such as video understanding, question answering, and reasoning, they still suffer from the problem of hallucination, which refers to generating outputs that are inconsistent with explicit video content or factual evidence. However, existing decoding methods for mitigating video hallucinations, while considering the spatiotemporal characteristics of videos, mostly rely on heuristic designs. As a result, they fail to precisely capture the root causes of hallucinations and their fine-grained temporal and semantic correlations, leading to limited robustness and generalization in complex scenarios. To more effectively mitigate video hallucinations, we propose a novel decoding strategy termed Spatiotemporal-Semantic Contrastive Decoding. This strategy constructs negative features by deliberately disrupting the spatiotemporal consistency and semantic associations of video features, and suppresses video hallucinations through contrastive decoding against the original video features during inference. Extensive experiments demonstrate that our method not only effectively mitigates the occurrence of hallucinations, but also preserves the general video understanding and reasoning capabilities of the model.

