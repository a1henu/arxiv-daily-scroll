---
layout: default
title: EntropyPrune: Matrix Entropy Guided Visual Token Pruning for Multimodal Large Language Models
---

# EntropyPrune: Matrix Entropy Guided Visual Token Pruning for Multimodal Large Language Models
**arXiv**：[2602.17196v1](https://arxiv.org/abs/2602.17196) · [PDF](https://arxiv.org/pdf/2602.17196.pdf)  
**作者**：Yahong Wang, Juncheng Wu, Zhangkai Ni, Chengmei Yang, Yihang Liu, Longzhen Yang, Yuyin Zhou, Ying Wen, Lianghua He  

**一句话要点**：提出基于矩阵熵的视觉令牌剪枝框架，以加速多模态大语言模型推理。

**关键词**：多模态大语言模型, 视觉令牌剪枝, 矩阵熵, 推理加速, 熵崩溃层

## 3 点简述
- 核心问题：多模态大语言模型推理成本高，现有令牌剪枝方法依赖启发式层选择，缺乏可解释性和可迁移性。
- 方法要点：引入矩阵熵视角，识别熵崩溃层作为剪枝阶段，量化令牌信息价值并剪枝冗余令牌，无需注意力图。
- 实验或效果：在LLaVA-1.5-7B上实现68.2% FLOPs减少，性能保留96.0%，泛化至高分辨率和视频模型。

## 摘要（原文）

> Multimodal large language models (MLLMs) incur substantial inference cost due to the processing of hundreds of visual tokens per image. Although token pruning has proven effective for accelerating inference, determining when and where to prune remains largely heuristic. Existing approaches typically rely on static, empirically selected layers, which limit interpretability and transferability across models. In this work, we introduce a matrix-entropy perspective and identify an "Entropy Collapse Layer" (ECL), where the information content of visual representations exhibits a sharp and consistent drop, which provides a principled criterion for selecting the pruning stage. Building on this observation, we propose EntropyPrune, a novel matrix-entropy-guided token pruning framework that quantifies the information value of individual visual tokens and prunes redundant ones without relying on attention maps. Moreover, to enable efficient computation, we exploit the spectral equivalence of dual Gram matrices, reducing the complexity of entropy computation and yielding up to a 64x theoretical speedup. Extensive experiments on diverse multimodal benchmarks demonstrate that EntropyPrune consistently outperforms state-of-the-art pruning methods in both accuracy and efficiency. On LLaVA-1.5-7B, our method achieves a 68.2% reduction in FLOPs while preserving 96.0% of the original performance. Furthermore, EntropyPrune generalizes effectively to high-resolution and video-based models, highlighting the strong robustness and scalability in practical MLLM acceleration. The code will be publicly available at https://github.com/YahongWang1/EntropyPrune.

