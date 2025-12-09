---
layout: default
title: Pay Less Attention to Function Words for Free Robustness of Vision-Language Models
---

# Pay Less Attention to Function Words for Free Robustness of Vision-Language Models
**arXiv**：[2512.07222v1](https://arxiv.org/abs/2512.07222) · [PDF](https://arxiv.org/pdf/2512.07222.pdf)  
**作者**：Qiwei Tian, Chenhao Lin, Zhengyu Zhao, Chao Shen  

**一句话要点**：提出函数词去注意力方法以提升视觉语言模型对抗跨模态攻击的鲁棒性

**关键词**：视觉语言模型, 对抗鲁棒性, 跨模态攻击, 注意力机制, 函数词处理, 零样本性能

## 3 点简述
- 核心问题：函数词导致视觉语言模型在跨模态对抗攻击下脆弱，需平衡鲁棒性与性能。
- 方法要点：设计函数词去注意力，在注意力头中计算原始与函数词交叉注意力并差分相减，增强对齐与鲁棒性。
- 实验效果：在检索和视觉定位任务上显著降低攻击成功率，性能下降极小或略有提升，验证了方法的可扩展性与泛化性。

## 摘要（原文）

> To address the trade-off between robustness and performance for robust VLM, we observe that function words could incur vulnerability of VLMs against cross-modal adversarial attacks, and propose Function-word De-Attention (FDA) accordingly to mitigate the impact of function words. Similar to differential amplifiers, our FDA calculates the original and the function-word cross-attention within attention heads, and differentially subtracts the latter from the former for more aligned and robust VLMs. Comprehensive experiments include 2 SOTA baselines under 6 different attacks on 2 downstream tasks, 3 datasets, and 3 models. Overall, our FDA yields an average 18/13/53% ASR drop with only 0.2/0.3/0.6% performance drops on the 3 tested models on retrieval, and a 90% ASR drop with a 0.3% performance gain on visual grounding. We demonstrate the scalability, generalization, and zero-shot performance of FDA experimentally, as well as in-depth ablation studies and analysis. Code will be made publicly at https://github.com/michaeltian108/FDA.

