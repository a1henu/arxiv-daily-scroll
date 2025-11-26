---
layout: default
title: BERT-APC: A Reference-free Framework for Automatic Pitch Correction via Musical Context Inference
---

# BERT-APC: A Reference-free Framework for Automatic Pitch Correction via Musical Context Inference
**arXiv**：[2511.20006v1](https://arxiv.org/abs/2511.20006) · [PDF](https://arxiv.org/pdf/2511.20006.pdf)  
**作者**：Sungjae Kim, Kihyun Na, Jinyoung Choi, Injung Kim  

**一句话要点**：提出BERT-APC框架，通过音乐上下文推理实现无参考音高校正

**关键词**：自动音高校正, 音乐语言模型, 无参考系统, 音高预测, 数据增强, 自然性保持

## 3 点简述
- 现有自动音高校正系统依赖参考音高或简单估计算法，难以保持自然性和表现力
- 结合固定音高预测器和上下文感知音高预测器，利用音乐语言模型推断意图音高序列
- 在高度失谐样本上音高预测准确率提升10.49%，MOS测试得分4.32，优于AutoTune和Melodyne

## 摘要（原文）

> Automatic Pitch Correction (APC) enhances vocal recordings by aligning pitch deviations with the intended musical notes. However, existing APC systems either rely on reference pitches, which limits their practical applicability, or employ simple pitch estimation algorithms that often fail to preserve expressiveness and naturalness. We propose BERT-APC, a novel reference-free APC framework that corrects pitch errors while maintaining the natural expressiveness of vocal performances. In BERT-APC, a novel stationary pitch predictor first estimates the perceived pitch of each note from the detuned singing voice. A context-aware note pitch predictor estimates the intended pitch sequence by leveraging a music language model repurposed to incorporate musical context. Finally, a note-level correction algorithm fixes pitch errors while preserving intentional pitch deviations for emotional expression. In addition, we introduce a learnable data augmentation strategy that improves the robustness of the music language model by simulating realistic detuning patterns. Compared to two recent singing voice transcription models, BERT-APC demonstrated superior performance in note pitch prediction, outperforming the second-best model, ROSVOT, by 10.49%p on highly detuned samples in terms of the raw pitch accuracy. In the MOS test, BERT-APC achieved the highest score of $4.32 \pm 0.15$, which is significantly higher than those of the widely-used commercial APC tools, AutoTune ($3.22 \pm 0.18$) and Melodyne ($3.08 \pm 0.18$), while maintaining a comparable ability to preserve expressive nuances. To the best of our knowledge, this is the first APC model that leverages a music language model to achieve reference-free pitch correction with symbolic musical context. The corrected audio samples of BERT-APC are available online.

