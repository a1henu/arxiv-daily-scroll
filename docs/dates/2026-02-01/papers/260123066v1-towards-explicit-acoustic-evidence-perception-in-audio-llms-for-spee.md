---
layout: default
title: Towards Explicit Acoustic Evidence Perception in Audio LLMs for Speech Deepfake Detection
---

# Towards Explicit Acoustic Evidence Perception in Audio LLMs for Speech Deepfake Detection
**arXiv**：[2601.23066v1](https://arxiv.org/abs/2601.23066) · [PDF](https://arxiv.org/pdf/2601.23066.pdf)  
**作者**：Xiaoxuan Guo, Yuankun Xie, Haonan Cheng, Jiayi Zhou, Jian Liu, Hengyan Huang, Long Ye, Qin Zhang  

**一句话要点**：提出SDD-APALLM框架，通过增强音频LLM的声学感知能力以提升语音深度伪造检测的准确性。

**关键词**：语音深度伪造检测, 音频大语言模型, 声学感知增强, 时间频率证据, 多模态融合

## 3 点简述
- 现有音频LLM方法偏向语义线索，忽略细粒度声学伪影，导致检测漏洞。
- 结合原始音频和结构化频谱图，显式暴露声学证据，平衡语义与声学推理。
- 实验显示检测精度和鲁棒性提升，尤其在语义误导场景下效果显著。

## 摘要（原文）

> Speech deepfake detection (SDD) focuses on identifying whether a given speech signal is genuine or has been synthetically generated. Existing audio large language model (LLM)-based methods excel in content understanding; however, their predictions are often biased toward semantically correlated cues, which results in fine-grained acoustic artifacts being overlooked during the decisionmaking process. Consequently, fake speech with natural semantics can bypass detectors despite harboring subtle acoustic anomalies; this suggests that the challenge stems not from the absence of acoustic data, but from its inadequate accessibility when semantic-dominant reasoning prevails. To address this issue, we investigate SDD within the audio LLM paradigm and introduce SDD with Auditory Perception-enhanced Audio Large Language Model (SDD-APALLM), an acoustically enhanced framework designed to explicitly expose fine-grained time-frequency evidence as accessible acoustic cues. By combining raw audio with structured spectrograms, the proposed framework empowers audio LLMs to more effectively capture subtle acoustic inconsistencies without compromising their semantic understanding. Experimental results indicate consistent gains in detection accuracy and robustness, especially in cases where semantic cues are misleading. Further analysis reveals that these improvements stem from a coordinated utilization of semantic and acoustic information, as opposed to simple modality aggregation.

