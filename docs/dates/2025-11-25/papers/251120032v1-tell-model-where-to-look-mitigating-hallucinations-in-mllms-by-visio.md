---
layout: default
title: Tell Model Where to Look: Mitigating Hallucinations in MLLMs by Vision-Guided Attention
---

# Tell Model Where to Look: Mitigating Hallucinations in MLLMs by Vision-Guided Attention
**arXiv**：[2511.20032v1](https://arxiv.org/abs/2511.20032) · [PDF](https://arxiv.org/pdf/2511.20032.pdf)  
**作者**：Jianfei Zhao, Feng Zhang, Xin Sun, Chong Feng, Zhixing Tan  

**一句话要点**：提出视觉引导注意力以缓解多模态大模型在图像理解中的幻觉问题

**关键词**：多模态大模型, 视觉引导注意力, 幻觉缓解, 图像描述生成, 训练无关方法

## 3 点简述
- 核心问题：MLLMs视觉注意力定位能力有限，导致生成内容出现幻觉。
- 方法要点：利用视觉令牌语义构建精确视觉基础，引导模型关注相关区域。
- 实验或效果：在多个基准测试中实现最先进的去幻觉性能，延迟仅增4.36%。

## 摘要（原文）

> Visual attention serves as the primary mechanism through which MLLMs interpret visual information; however, its limited localization capability often leads to hallucinations. We observe that although MLLMs can accurately extract visual semantics from visual tokens, they fail to fully leverage this advantage during subsequent inference. To address this limitation, we propose Vision-Guided Attention (VGA), a training-free method that first constructs precise visual grounding by exploiting the semantic content of visual tokens, and then uses this grounding to guide the model's focus toward relevant visual regions. In image captioning, VGA further refines this guidance dynamically during generation by suppressing regions that have already been described. In VGA, each token undergoes only a single forward pass, introducing a negligible latency overhead of just 4.36\%. In addition, VGA is fully compatible with efficient attention implementations such as FlashAttention. Extensive experiments across diverse MLLMs and multiple hallucination benchmarks demonstrate that VGA achieves state-of-the-art dehallucination performance. Further analysis confirms that explicit visual guidance plays a crucial role in enhancing the visual understanding capabilities of MLLMs.

