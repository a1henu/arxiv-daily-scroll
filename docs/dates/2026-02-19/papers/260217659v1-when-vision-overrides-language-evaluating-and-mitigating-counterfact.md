---
layout: default
title: When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs
---

# When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs
**arXiv**：[2602.17659v1](https://arxiv.org/abs/2602.17659) · [PDF](https://arxiv.org/pdf/2602.17659.pdf)  
**作者**：Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding  

**一句话要点**：提出Counterfactual Action Guidance以缓解视觉-语言-动作模型中的反事实失败问题

**关键词**：视觉-语言-动作模型, 反事实失败, 语言遵循能力, 双分支推理, 机器人控制, 基准评估

## 3 点简述
- 核心问题：视觉-语言-动作模型在缺乏场景特定监督时，因数据集偏见导致反事实失败，忽视语言指令而依赖视觉捷径。
- 方法要点：引入Counterfactual Action Guidance，通过双分支推理方案结合标准策略和语言无条件视觉-动作模块，显式正则化语言条件。
- 实验或效果：在LIBERO-CF基准上显著提升语言遵循准确性和任务成功率，并在真实世界评估中减少反事实失败。

## 摘要（原文）

> Vision-Language-Action models (VLAs) promise to ground language instructions in robot control, yet in practice often fail to faithfully follow language. When presented with instructions that lack strong scene-specific supervision, VLAs suffer from counterfactual failures: they act based on vision shortcuts induced by dataset biases, repeatedly executing well-learned behaviors and selecting objects frequently seen during training regardless of language intent. To systematically study it, we introduce LIBERO-CF, the first counterfactual benchmark for VLAs that evaluates language following capability by assigning alternative instructions under visually plausible LIBERO layouts. Our evaluation reveals that counterfactual failures are prevalent yet underexplored across state-of-the-art VLAs. We propose Counterfactual Action Guidance (CAG), a simple yet effective dual-branch inference scheme that explicitly regularizes language conditioning in VLAs. CAG combines a standard VLA policy with a language-unconditioned Vision-Action (VA) module, enabling counterfactual comparison during action selection. This design reduces reliance on visual shortcuts, improves robustness on under-observed tasks, and requires neither additional demonstrations nor modifications to existing architectures or pretrained models. Extensive experiments demonstrate its plug-and-play integration across diverse VLAs and consistent improvements. For example, on LIBERO-CF, CAG improves $π_{0.5}$ by 9.7% in language following accuracy and 3.6% in task success on under-observed tasks using a training-free strategy, with further gains of 15.5% and 8.5%, respectively, when paired with a VA model. In real-world evaluations, CAG reduces counterfactual failures of 9.4% and improves task success by 17.2% on average.

