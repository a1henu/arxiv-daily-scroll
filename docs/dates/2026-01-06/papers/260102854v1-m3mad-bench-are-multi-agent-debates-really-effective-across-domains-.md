---
layout: default
title: M3MAD-Bench: Are Multi-Agent Debates Really Effective Across Domains and Modalities?
---

# M3MAD-Bench: Are Multi-Agent Debates Really Effective Across Domains and Modalities?
**arXiv**：[2601.02854v1](https://arxiv.org/abs/2601.02854) · [PDF](https://arxiv.org/pdf/2601.02854.pdf)  
**作者**：Ao Li, Jinghui Zhang, Luyu Li, Yuxiang Duan, Lang Gao, Mingcai Chen, Weijun Qin, Shaopeng Li, Fengxian Ji, Ning Liu, Lizhen Cui, Xiuying Chen, Yuntao Du  

**一句话要点**：提出M3MAD-Bench基准以解决多智能体辩论评估的碎片化和单模态限制问题。

**关键词**：多智能体辩论, 多模态评估, 基准测试, 标准化协议, 性能-成本权衡

## 3 点简述
- 核心问题：现有MAD评估设置碎片化且局限于单模态文本输入，阻碍公平比较。
- 方法要点：建立统一基准，覆盖多领域任务、多模态输入和多维度指标，支持标准化评估。
- 实验或效果：在九个基础模型上评估，提供性能-成本权衡的系统性洞察，促进未来研究。

## 摘要（原文）

> As an agent-level reasoning and coordination paradigm, Multi-Agent Debate (MAD) orchestrates multiple agents through structured debate to improve answer quality and support complex reasoning. However, existing research on MAD suffers from two fundamental limitations: evaluations are conducted under fragmented and inconsistent settings, hindering fair comparison, and are largely restricted to single-modality scenarios that rely on textual inputs only. To address these gaps, we introduce M3MAD-Bench, a unified and extensible benchmark for evaluating MAD methods across Multi-domain tasks, Multi-modal inputs, and Multi-dimensional metrics. M3MAD-Bench establishes standardized protocols over five core task domains: Knowledge, Mathematics, Medicine, Natural Sciences, and Complex Reasoning, and systematically covers both pure text and vision-language datasets, enabling controlled cross-modality comparison. We evaluate MAD methods on nine base models spanning different architectures, scales, and modality capabilities. Beyond accuracy, M3MAD-Bench incorporates efficiency-oriented metrics such as token consumption and inference time, providing a holistic view of performance--cost trade-offs. Extensive experiments yield systematic insights into the effectiveness, robustness, and efficiency of MAD across text-only and multimodal scenarios. We believe M3MAD-Bench offers a reliable foundation for future research on standardized MAD evaluation. The code is available at http://github.com/liaolea/M3MAD-Bench.

