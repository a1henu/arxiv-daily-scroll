---
layout: default
title: OPV: Outcome-based Process Verifier for Efficient Long Chain-of-Thought Verification
---

# OPV: Outcome-based Process Verifier for Efficient Long Chain-of-Thought Verification
**arXiv**：[2512.10756v1](https://arxiv.org/abs/2512.10756) · [PDF](https://arxiv.org/pdf/2512.10756.pdf)  
**作者**：Zijian Wu, Lingkai Kong, Wenwei Zhang, Songyang Gao, Yuzhe Gu, Zhongrui Cai, Tianyou Ma, Yuhong Liu, Zhi Wang, Runyuan Ma, Guangyu Wang, Wei Li, Conghui He, Dahua Lin, Kai Chen  

**一句话要点**：提出基于结果的流程验证器OPV，通过总结长思维链结果来高效验证推理过程

**关键词**：思维链验证, 结果导向验证, 主动学习, 拒绝微调, 强化学习验证奖励, 大规模标注

## 3 点简述
- 当前基于结果的验证器无法检查长思维链中的不可靠中间步骤，而基于流程的验证器受限于标注成本难以可靠检测复杂长链错误
- OPV通过验证长思维链总结结果的推理过程，结合迭代主动学习框架和专家标注，以较低成本提升验证能力
- 在OPV-Bench上取得83.1的F1分数，优于Qwen3-Max-Preview的76.3，并能有效提升策略模型性能

## 摘要（原文）

> Large language models (LLMs) have achieved significant progress in solving complex reasoning tasks by Reinforcement Learning with Verifiable Rewards (RLVR). This advancement is also inseparable from the oversight automated by reliable verifiers. However, current outcome-based verifiers (OVs) are unable to inspect the unreliable intermediate steps in the long reasoning chains of thought (CoTs). Meanwhile, current process-based verifiers (PVs) have difficulties in reliably detecting errors in the complex long CoTs, limited by the scarcity of high-quality annotations due to the prohibitive costs of human annotations. Therefore, we propose the Outcome-based Process Verifier (OPV), which verifies the rationale process of summarized outcomes from long CoTs to achieve both accurate and efficient verification and enable large-scale annotation. To empower the proposed verifier, we adopt an iterative active learning framework with expert annotations to progressively improve the verification capability of OPV with fewer annotation costs. Specifically, in each iteration, the most uncertain cases of the current best OPV are annotated and then subsequently used to train a new OPV through Rejection Fine-Tuning (RFT) and RLVR for the next round. Extensive experiments demonstrate OPV's superior performance and broad applicability. It achieves new state-of-the-art results on our held-out OPV-Bench, outperforming much larger open-source models such as Qwen3-Max-Preview with an F1 score of 83.1 compared to 76.3. Furthermore, OPV effectively detects false positives within synthetic dataset, closely align with expert assessment. When collaborating with policy models, OPV consistently yields performance gains, e.g., raising the accuracy of DeepSeek-R1-Distill-Qwen-32B from 55.2% to 73.3% on AIME2025 as the compute budget scales.

