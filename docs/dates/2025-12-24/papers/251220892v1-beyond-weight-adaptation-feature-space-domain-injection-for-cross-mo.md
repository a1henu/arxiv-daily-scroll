---
layout: default
title: Beyond Weight Adaptation: Feature-Space Domain Injection for Cross-Modal Ship Re-Identification
---

# Beyond Weight Adaptation: Feature-Space Domain Injection for Cross-Modal Ship Re-Identification
**arXiv**：[2512.20892v1](https://arxiv.org/abs/2512.20892) · [PDF](https://arxiv.org/pdf/2512.20892.pdf)  
**作者**：Tingfeng Xian, Wenlve Zhou, Zhiheng Zhou, Zhelin Li  

**一句话要点**：提出特征空间域注入方法以解决跨模态船舶重识别中的模态差异问题

**关键词**：跨模态船舶重识别, 特征空间优化, 参数高效微调, 视觉基础模型, 域表示注入

## 3 点简述
- 核心问题：跨模态船舶重识别面临显著模态差异，依赖大规模配对数据预训练。
- 方法要点：基于视觉基础模型，设计轻量偏移编码器和调制器，在特征空间注入域特定表示。
- 实验或效果：在HOSS-ReID数据集上以少量参数实现SOTA性能，如1.54M参数达57.9% mAP。

## 摘要（原文）

> Cross-Modality Ship Re-Identification (CMS Re-ID) is critical for achieving all-day and all-weather maritime target tracking, yet it is fundamentally challenged by significant modality discrepancies. Mainstream solutions typically rely on explicit modality alignment strategies; however, this paradigm heavily depends on constructing large-scale paired datasets for pre-training. To address this, grounded in the Platonic Representation Hypothesis, we explore the potential of Vision Foundation Models (VFMs) in bridging modality gaps. Recognizing the suboptimal performance of existing generic Parameter-Efficient Fine-Tuning (PEFT) methods that operate within the weight space, particularly on limited-capacity models, we shift the optimization perspective to the feature space and propose a novel PEFT strategy termed Domain Representation Injection (DRI). Specifically, while keeping the VFM fully frozen to maximize the preservation of general knowledge, we design a lightweight, learnable Offset Encoder to extract domain-specific representations rich in modality and identity attributes from raw inputs. Guided by the contextual information of intermediate features at different layers, a Modulator adaptively transforms these representations. Subsequently, they are injected into the intermediate layers via additive fusion, dynamically reshaping the feature distribution to adapt to the downstream task without altering the VFM's pre-trained weights. Extensive experimental results demonstrate the superiority of our method, achieving State-of-the-Art (SOTA) performance with minimal trainable parameters. For instance, on the HOSS-ReID dataset, we attain 57.9\% and 60.5\% mAP using only 1.54M and 7.05M parameters, respectively. The code is available at https://github.com/TingfengXian/DRI.

