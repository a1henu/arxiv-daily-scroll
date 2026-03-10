---
layout: default
title: Local-Global Prompt Learning via Sparse Optimal Transport
---

# Local-Global Prompt Learning via Sparse Optimal Transport
**arXiv**：[2603.08347v1](https://arxiv.org/abs/2603.08347) · [PDF](https://arxiv.org/pdf/2603.08347.pdf)  
**作者**：Deniz Kizaroğlu, Ülku Tuncer Küçüktas, Emre Çakmakyurdu, Alptekin Temizel  

**一句话要点**：提出SOT-GLP方法，通过稀疏最优运输实现局部-全局提示学习，以解决少样本视觉语言模型适应中的局部特征冗余问题。

**关键词**：视觉语言模型, 少样本学习, 提示学习, 稀疏最优运输, 异常检测

## 3 点简述
- 核心问题：现有方法在少样本适应中独立选择局部区域，导致局部特征冗余和提示重叠，影响细粒度视觉线索利用。
- 方法要点：引入共享稀疏补丁支持和平衡最优运输分配，显式划分显著视觉区域给类别特定局部提示，同时保持全局对齐。
- 实验或效果：在11个标准基准上，16-shot ViT-B/16达到85.1%平均准确率，优于先前方法；在OOD检测中实现94.2% AUC，表现优异。

## 摘要（原文）

> Few-shot adaptation of vision-language models (VLMs) like CLIP typically relies on learning textual prompts matched to global image embeddings. Recent works extend this paradigm by incorporating local image-text alignment to capture fine-grained visual cues, yet these approaches often select local regions independently for each prompt, leading to redundant local feature usage and prompt overlap. We propose SOT-GLP, which introduces a shared sparse patch support and balanced optimal transport allocation to explicitly partition salient visual regions among class-specific local prompts while preserving global alignment. Our method learns shared global prompts and class-specific local prompts. The global branch maintains standard image-text matching for robust category-level alignment. The local branch constructs a class-conditioned sparse patch set using V-V attention and aligns it to multiple class-specific prompts via balanced entropic optimal transport, yielding a soft partition of patches that prevents prompt overlap and collapse. We evaluate our method on two complementary objectives: (i) few-shot classification accuracy on 11 standard benchmarks and (ii) out-of-distribution (OOD) detection. On the standard 11-dataset benchmark with 16-shot ViT-B/16, SOT-GLP achieves 85.1% average accuracy, outperforming prior prompt-learning methods. We identify a distinct accuracy-robustness trade-off in prompt learning: while learnable projections optimize in-distribution fit, they alter the foundational feature space. We demonstrate that a projection-free local alignment preserves the native geometry of the CLIP manifold, yielding state-of-the-art OOD detection performance (94.2% AUC) that surpasses fully adapted models. Implementation available at: https://github.com/Deniz2304988/SOT-GLP

