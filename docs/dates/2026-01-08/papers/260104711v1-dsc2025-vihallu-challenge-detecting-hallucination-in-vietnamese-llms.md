---
layout: default
title: DSC2025 -- ViHallu Challenge: Detecting Hallucination in Vietnamese LLMs
---

# DSC2025 -- ViHallu Challenge: Detecting Hallucination in Vietnamese LLMs
**arXiv**：[2601.04711v1](https://arxiv.org/abs/2601.04711) · [PDF](https://arxiv.org/pdf/2601.04711.pdf)  
**作者**：Anh Thi-Hoang Nguyen, Khanh Quoc Tran, Tin Van Huynh, Phuoc Tan-Hoang Nguyen, Cam Tan Nguyen, Kiet Van Nguyen  

**一句话要点**：提出DSC2025 ViHallu挑战赛与ViHallu数据集，以检测越南语大语言模型的幻觉问题。

**关键词**：幻觉检测, 越南语大语言模型, 基准数据集, 提示工程, 模型鲁棒性, 共享任务

## 3 点简述
- 核心问题：越南语等低资源语言缺乏标准化幻觉检测基准，影响LLMs可靠性。
- 方法要点：构建10,000个标注样本，分三类幻觉，含三种提示类型以测试模型鲁棒性。
- 实验或效果：111支队伍参与，最佳系统宏F1达84.80%，但内在幻觉检测仍具挑战性。

## 摘要（原文）

> The reliability of large language models (LLMs) in production environments remains significantly constrained by their propensity to generate hallucinations -- fluent, plausible-sounding outputs that contradict or fabricate information. While hallucination detection has recently emerged as a priority in English-centric benchmarks, low-to-medium resource languages such as Vietnamese remain inadequately covered by standardized evaluation frameworks. This paper introduces the DSC2025 ViHallu Challenge, the first large-scale shared task for detecting hallucinations in Vietnamese LLMs. We present the ViHallu dataset, comprising 10,000 annotated triplets of (context, prompt, response) samples systematically partitioned into three hallucination categories: no hallucination, intrinsic, and extrinsic hallucinations. The dataset incorporates three prompt types -- factual, noisy, and adversarial -- to stress-test model robustness. A total of 111 teams participated, with the best-performing system achieving a macro-F1 score of 84.80\%, compared to a baseline encoder-only score of 32.83\%, demonstrating that instruction-tuned LLMs with structured prompting and ensemble strategies substantially outperform generic architectures. However, the gap to perfect performance indicates that hallucination detection remains a challenging problem, particularly for intrinsic (contradiction-based) hallucinations. This work establishes a rigorous benchmark and explores a diverse range of detection methodologies, providing a foundation for future research into the trustworthiness and reliability of Vietnamese language AI systems.

