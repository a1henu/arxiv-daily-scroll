---
layout: default
title: ForgetMark: Stealthy Fingerprint Embedding via Targeted Unlearning in Language Models
---

# ForgetMark: Stealthy Fingerprint Embedding via Targeted Unlearning in Language Models
**arXiv**：[2601.08189v1](https://arxiv.org/abs/2601.08189) · [PDF](https://arxiv.org/pdf/2601.08189.pdf)  
**作者**：Zhenhua Xu, Haobo Zhang, Zhebo Wang, Qichen Liu, Haitao Xu, Wenpeng Xing, Meng Han  

**一句话要点**：提出ForgetMark框架，通过目标遗忘在语言模型中嵌入隐蔽指纹以解决溯源问题。

**关键词**：语言模型指纹, 目标遗忘, LoRA适配器, 所有权验证, 隐蔽性, 模型溯源

## 3 点简述
- 现有侵入式指纹存在高困惑度触发词易被过滤、固定响应模式易被检测等问题。
- ForgetMark利用目标遗忘编码溯源信息，构建紧凑可读键值集并训练LoRA适配器抑制原值。
- 实验显示在多种架构下实现100%所有权验证，保持标准性能，并提升隐蔽性和鲁棒性。

## 摘要（原文）

> Existing invasive (backdoor) fingerprints suffer from high-perplexity triggers that are easily filtered, fixed response patterns exposed by heuristic detectors, and spurious activations on benign inputs. We introduce \textsc{ForgetMark}, a stealthy fingerprinting framework that encodes provenance via targeted unlearning. It builds a compact, human-readable key--value set with an assistant model and predictive-entropy ranking, then trains lightweight LoRA adapters to suppress the original values on their keys while preserving general capabilities. Ownership is verified under black/gray-box access by aggregating likelihood and semantic evidence into a fingerprint success rate. By relying on probabilistic forgetting traces rather than fixed trigger--response patterns, \textsc{ForgetMark} avoids high-perplexity triggers, reduces detectability, and lowers false triggers. Across diverse architectures and settings, it achieves 100\% ownership verification on fingerprinted models while maintaining standard performance, surpasses backdoor baselines in stealthiness and robustness to model merging, and remains effective under moderate incremental fine-tuning. Our code and data are available at \href{https://github.com/Xuzhenhua55/ForgetMark}{https://github.com/Xuzhenhua55/ForgetMark}.

