---
layout: default
title: Robust TTS Training via Self-Purifying Flow Matching for the WildSpoof 2026 TTS Track
---

# Robust TTS Training via Self-Purifying Flow Matching for the WildSpoof 2026 TTS Track
**arXiv**：[2512.17293v1](https://arxiv.org/abs/2512.17293) · [PDF](https://arxiv.org/pdf/2512.17293.pdf)  
**作者**：June Young Yi, Hyeongju Kim, Juheon Lee  

**一句话要点**：提出自净化流匹配方法，用于在WildSpoof挑战中增强TTS模型对野外语音的鲁棒性。

**关键词**：文本到语音, 流匹配, 噪声处理, 模型微调, 鲁棒性训练, 语音合成

## 3 点简述
- 核心问题：TTS模型在野外语音条件下易受标签噪声影响，导致性能下降。
- 方法要点：通过比较条件与无条件流匹配损失，筛选可疑样本进行无条件训练，保留声学信息。
- 实验或效果：在Word Error Rate上取得最佳成绩，在UTMOS和DNSMOS感知指标中排名第二。

## 摘要（原文）

> This paper presents a lightweight text-to-speech (TTS) system developed for the WildSpoof Challenge TTS Track. Our approach fine-tunes the recently released open-weight TTS model, \textit{Supertonic}\footnote{\url{https://github.com/supertone-inc/supertonic}}, with Self-Purifying Flow Matching (SPFM) to enable robust adaptation to in-the-wild speech. SPFM mitigates label noise by comparing conditional and unconditional flow matching losses on each sample, routing suspicious text--speech pairs to unconditional training while still leveraging their acoustic information. The resulting model achieves the lowest Word Error Rate (WER) among all participating teams, while ranking second in perceptual metrics such as UTMOS and DNSMOS. These findings demonstrate that efficient, open-weight architectures like Supertonic can be effectively adapted to diverse real-world speech conditions when combined with explicit noise-handling mechanisms such as SPFM.

