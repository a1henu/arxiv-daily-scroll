---
layout: default
title: KVSmooth: Mitigating Hallucination in Multi-modal Large Language Models through Key-Value Smoothing
---

# KVSmooth: Mitigating Hallucination in Multi-modal Large Language Models through Key-Value Smoothing
**arXiv**：[2602.04268v1](https://arxiv.org/abs/2602.04268) · [PDF](https://arxiv.org/pdf/2602.04268.pdf)  
**作者**：Siyu Jiang, Feiyang Chen, Xiaojin Zhang, Kun He  

**一句话要点**：提出KVSmooth方法，通过键值平滑缓解多模态大语言模型中的幻觉问题

**关键词**：多模态大语言模型, 幻觉缓解, 键值平滑, 注意力熵, 推理优化, 训练无关方法

## 3 点简述
- 核心问题：多模态大语言模型在解码时语义漂移，导致幻觉（视觉不一致生成）
- 方法要点：基于注意力熵引导的自适应平滑，对KV-Cache中的键值应用指数移动平均
- 实验或效果：显著降低幻觉指标（CHAIR_S从41.8降至18.2），同时提升整体性能（F1分数从77.5升至79.2）

## 摘要（原文）

> Despite the significant progress of Multimodal Large Language Models (MLLMs) across diverse tasks, hallucination -- corresponding to the generation of visually inconsistent objects, attributes, or relations -- remains a major obstacle to their reliable deployment. Unlike pure language models, MLLMs must ground their generation process in visual inputs. However, existing models often suffer from semantic drift during decoding, causing outputs to diverge from visual facts as the sequence length increases.
>   To address this issue, we propose KVSmooth, a training-free and plug-and-play method that mitigates hallucination by performing attention-entropy-guided adaptive smoothing on hidden states. Specifically, KVSmooth applies an exponential moving average (EMA) to both keys and values in the KV-Cache, while dynamically quantifying the sink degree of each token through the entropy of its attention distribution to adaptively adjust the smoothing strength.
>   Unlike computationally expensive retraining or contrastive decoding methods, KVSmooth operates efficiently during inference without additional training or model modification. Extensive experiments demonstrate that KVSmooth significantly reduces hallucination ($\mathit{CHAIR}_{S}$ from $41.8 \rightarrow 18.2$) while improving overall performance ($F_1$ score from $77.5 \rightarrow 79.2$), achieving higher precision and recall simultaneously. In contrast, prior methods often improve one at the expense of the other, validating the effectiveness and generality of our approach.

