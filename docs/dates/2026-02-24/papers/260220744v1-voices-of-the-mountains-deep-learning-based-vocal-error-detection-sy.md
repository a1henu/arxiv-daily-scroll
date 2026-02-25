---
layout: default
title: Voices of the Mountains: Deep Learning-Based Vocal Error Detection System for Kurdish Maqams
---

# Voices of the Mountains: Deep Learning-Based Vocal Error Detection System for Kurdish Maqams
**arXiv**：[2602.20744v1](https://arxiv.org/abs/2602.20744) · [PDF](https://arxiv.org/pdf/2602.20744.pdf)  
**作者**：Darvan Shvan Khairaldeen, Hossein Hassani  

**一句话要点**：提出基于深度学习的库尔德木卡姆声乐错误检测系统，以解决西方音乐规则下微音程和音高弯曲的识别问题。

**关键词**：自动歌唱评估, 库尔德木卡姆, 微音程检测, CNN-BiLSTM, 注意力机制, 声乐错误分类

## 3 点简述
- 核心问题：现有自动歌唱评估工具基于西方音乐规则，无法检测库尔德木卡姆中的微音程和音高弯曲，导致误判。
- 方法要点：使用CNN-BiLSTM加注意力机制的双头模型，从对数梅尔频谱图中检测和分类音高、节奏和调式稳定性错误。
- 实验或效果：在50首歌曲数据集上验证，模型在常见错误类型上表现较好，但调式漂移召回率低，需更多数据和平衡。

## 摘要（原文）

> Maqam, a singing type, is a significant component of Kurdish music. A maqam singer receives training in a traditional face-to-face or through self-training. Automatic Singing Assessment (ASA) uses machine learning (ML) to provide the accuracy of singing styles and can help learners to improve their performance through error detection. Currently, the available ASA tools follow Western music rules. The musical composition requires all notes to stay within their expected pitch range from start to finish. The system fails to detect micro-intervals and pitch bends, so it identifies Kurdish maqam singing as incorrect even though the singer performs according to traditional rules. Kurdish maqam requires recognizing performance errors within microtonal spaces, which is beyond Western equal temperament. This research is the first attempt to address the mentioned gap. While many error types happen during singing, our focus is on pitch, rhythm, and modal stability errors in the context of Bayati-Kurd. We collected 50 songs from 13 vocalists ( 2-3 hours) and annotated 221 error spans (150 fine pitch, 46 rhythm, 25 modal drift). The data was segmented into 15,199 overlapping windows and converted to log-mel spectrograms. We developed a two-headed CNN-BiLSTM with attention mode to decide whether a window contains an error and to classify it based on the chosen errors. Trained for 20 epochs with early stopping at epoch 10, the model reached a validation macro-F1 of 0.468. On the full 50-song evaluation at a 0.750 threshold, recall was 39.4% and precision 25.8% . Within detected windows, type macro-F1 was 0.387, with F1 of 0.492 (fine pitch), 0.536 (rhythm), and 0.133 (modal drift); modal drift recall was 8.0%. The better performance on common error types shows that the method works, while the poor modal-drift recall shows that more data and balancing are needed.

