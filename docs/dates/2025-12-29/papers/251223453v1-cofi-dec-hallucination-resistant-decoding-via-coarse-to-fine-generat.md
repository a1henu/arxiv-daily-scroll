---
layout: default
title: CoFi-Dec: Hallucination-Resistant Decoding via Coarse-to-Fine Generative Feedback in Large Vision-Language Models
---

# CoFi-Dec: Hallucination-Resistant Decoding via Coarse-to-Fine Generative Feedback in Large Vision-Language Models
**arXiv**：[2512.23453v1](https://arxiv.org/abs/2512.23453) · [PDF](https://arxiv.org/pdf/2512.23453.pdf)  
**作者**：Zongsheng Cao, Yangfan He, Anran Liu, Jun Xie, Feng Chen, Zepeng Wang  

**一句话要点**：提出CoFi-Dec解码框架，通过粗到细生成反馈减少大视觉语言模型的幻觉问题

**关键词**：大视觉语言模型, 幻觉缓解, 解码策略, 生成反馈, 视觉条件, Wasserstein融合

## 3 点简述
- 核心问题：大视觉语言模型易产生与视觉输入不一致的幻觉内容，影响可靠性
- 方法要点：基于粗到细视觉条件生成中间响应，利用文本到图像模型合成多级视觉假设，通过Wasserstein融合统一预测
- 实验或效果：在六个幻觉基准测试中显著减少实体和语义级幻觉，无需额外训练且模型无关

## 摘要（原文）

> Large Vision-Language Models (LVLMs) have achieved impressive progress in multi-modal understanding and generation. However, they still tend to produce hallucinated content that is inconsistent with the visual input, which limits their reliability in real-world applications. We propose \textbf{CoFi-Dec}, a training-free decoding framework that mitigates hallucinations by integrating generative self-feedback with coarse-to-fine visual conditioning. Inspired by the human visual process from global scene perception to detailed inspection, CoFi-Dec first generates two intermediate textual responses conditioned on coarse- and fine-grained views of the original image. These responses are then transformed into synthetic images using a text-to-image model, forming multi-level visual hypotheses that enrich grounding cues. To unify the predictions from these multiple visual conditions, we introduce a Wasserstein-based fusion mechanism that aligns their predictive distributions into a geometrically consistent decoding trajectory. This principled fusion reconciles high-level semantic consistency with fine-grained visual grounding, leading to more robust and faithful outputs. Extensive experiments on six hallucination-focused benchmarks show that CoFi-Dec substantially reduces both entity-level and semantic-level hallucinations, outperforming existing decoding strategies. The framework is model-agnostic, requires no additional training, and can be seamlessly applied to a wide range of LVLMs. The implementation is available at https://github.com/AI-Researcher-Team/CoFi-Dec.

